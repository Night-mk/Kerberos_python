#!/usr/bin/env python3
#
# Author:
#  Tamas Jos (@skelsec)
#
#!/usr/bin/env python3
#
# Author:
#  Tamas Jos (@skelsec)
#
import json
import collections
import datetime
import secrets
import socket
import logging
import pickle
from minikerberos.RC4 import *
class KerberosCredential:
	def __init__(self):
		self.username = None
		self.domain = None
		self.password = None
		self.nt_hash = None
		self.lm_hash = None
		self.kerberos_key_aes_256 = None
		self.kerberos_key_aes_128 = None
		self.kerberos_key_des = None
		self.kerberos_key_rc4 = None
class KerbrosComm:
	def __init__(self,ccred):
		self.usercreds = ccred
		#self.ksoc = ksoc
		self.kerberos_session_key = None
		self.kerberos_TGT = None
		self.kerberos_TGT_encpart = None
		self.kerberos_TGS = None
		self.time1 = None
		self.Ekc = '3'
	@staticmethod

	def get_TGT(self):
		"""
		decrypt_tgt: used for asreproast attacks
		Steps performed:
			1. Send and empty (no encrypted timestamp) AS_REQ with all the encryption types we support
			2. Depending on the response (either error or AS_REP with TGT) we either send another AS_REQ with the encrypted data or return the TGT (or fail miserably)
			3. PROFIT
		"""
		logger.debug('Generating initial TGT without authentication data')
		now = datetime.datetime.utcnow()
		kdc_req_body = {}
		kdc_req_body['IDC'] = self.usercreds.username
		kdc_req_body['TS2'] = now.strftime('%Y-%m-%d %H-%M-%S')
		kdc_req_body['Kc2tgs'] = str(secrets.randbits(31))
		kdc_req_body['lefttime2'] = 'oneday'
		Ticket_tgs_file=json.dumps(kdc_req_body)
		Ticket_tgs=rc4_main_en('3',Ticket_tgs_file)
		first_TGT={}
		TGT={}
		first_TGT['Kc2tgs']=kdc_req_body['Kc2tgs']
		first_TGT['TS2']=kdc_req_body['TS2']
		first_TGT['lefttime2']=kdc_req_body['lefttime2']
		first_TGT['Ticket_tgs']=Ticket_tgs
		#print(first_TGT['Ticket_tgs'])
		first_TGT_file=json.dumps(first_TGT)
		TGT=rc4_main_en(self.Ekc,first_TGT_file)
		#print(TGT)
		return TGT
		#默认Ektgs=3

		
	def creat_Authenticator_c(username,IDO,Kc2tgs,TS3= None):

		now=datetime.datetime.utcnow()

		Authenticator_c_body={}
		Authenticator_c_body['IDC']=self.usercreds.username
		Authenticator_c_body['IDO']=IDO
		Authenticator_c_body['TS3']=now.strftime('%Y-%m-%d %H-%M-%S')
		Authenticator_c_body_file=json.dumps(Authenticator_c_body)
		Authenticator_c=rc4_main_en(Kc2tgs,Authenticator_c_body_file)
		return Authenticator_c,Authenticator_c_body['TS3']
		
	def get_TGS(self, IDO, IDV, Ticket_tgs,Authenticator_c):
		"""
		Requests a TGS ticket for the specified user.
		Retruns the TGS ticket, end the decrpyted encTGSRepPart.

		spn_user: KerberosTarget: the service user you want to get TGS for.
		override_etype: None or list of etype values (int) Used mostly for kerberoasting, will override the AP_REQ supported etype values (which is derived from the TGT) to be able to recieve whatever tgs tiecket 
		"""
		#construct tgs_req
		#logger.debug('Constructing TGS request for user %s' % spn_user.get_formatted_pname())
		#默认Ektgs=3
		Ticket_tgs_body=Ticket_tgs
		TGT=rc4_main_de(self.Ekc,Ticket_tgs_body)
		now = datetime.datetime.utcnow() 
		kdc_req_body = {}#IDO,IDV,Ticket_tgs,Authenticator_c
		kdc_req_body['IDO'] = IDO
		kdc_req_body['IDV'] = IDV
		kdc_req_body['Ticket_tgs'] = Ticket_tgs
		kdc_req_body['Authenticator_c'] = Authenticator_c
		Ticket_tgs_body_file={}
		Ticket_tgs_body_file=rc4_main_de('3',Ticket_tgs)
		Ticket_tgs_body={}#IDC,TS2,Kc2tgs,lefttime2
		Ticket_tgs_body=json.loads(Ticket_tgs_body_file)
		Authenticator_c_body_file={}
		Authenticator_c_body={}#IDC,IDO,TS3
		Authenticator_c_body_file=rc4_main_de(Ticket_tgs_body['Kc2tgs'],kdc_req_body['Authenticator_c'])
		Authenticator_c_body=json.loads(Authenticator_c_body_file)
		Ticket_v_body={}#Kcv,IDC,IDO,IDV,TS4,lifetime4,ACc
		Ticket_v_body['Kcv']=str(secrets.randbits(31))
		Ticket_v_body['IDC']=Ticket_tgs_body['IDC']
		Ticket_v_body['IDO']=Authenticator_c_body['IDO']
		Ticket_v_body['IDV']=kdc_req_body['IDV']
		Ticket_v_body['TS4']=now.strftime('%Y-%m-%d %H-%M-%S')
		Ticket_v_body['lifetime4']='100'
		Ticket_v_body['ACc']=''
		Ticket_v_file=json.dumps(Ticket_v_body)
		Ticket_v=rc4_main_en('3',Ticket_v_file)
		TGS_body={}#Kcv,IDO,IDV,TS4,Ticket_v
		TGS_body['Kcv']=Ticket_v_body['Kcv']
		TGS_body['IDO']=Ticket_v_body['IDO']
		TGS_body['IDV']=Ticket_v_body['IDV']
		TGS_body['TS4']=Ticket_v_body['TS4']
		TGS_body['Ticket_v']=Ticket_v
		TGS_body_file=json.dumps(TGS_body)
		TGS=rc4_main_en(Ticket_tgs_body['Kc2tgs'],Ticket_v_file)

		return TGS
	
	#https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-sfu/6a8dfc0c-2d32-478a-929f-5f9b1b18a169

