<!DOCTYPE html>
<html>
<head>
<title>API.md</title>
<meta http-equiv="Content-type" content="text/html;charset=UTF-8">

<style>
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

body {
	font-family: "Segoe WPC", "Segoe UI", "SFUIText-Light", "HelveticaNeue-Light", sans-serif, "Droid Sans Fallback";
	font-size: 14px;
	padding: 0 12px;
	line-height: 22px;
	word-wrap: break-word;
}

#code-csp-warning {
	position: fixed;
	top: 0;
	right: 0;
	color: white;
	margin: 16px;
	text-align: center;
	font-size: 12px;
	font-family: sans-serif;
	background-color:#444444;
	cursor: pointer;
	padding: 6px;
	box-shadow: 1px 1px 1px rgba(0,0,0,.25);
}

#code-csp-warning:hover {
	text-decoration: none;
	background-color:#007acc;
	box-shadow: 2px 2px 2px rgba(0,0,0,.25);
}


body.scrollBeyondLastLine {
	margin-bottom: calc(100vh - 22px);
}

body.showEditorSelection .code-line {
	position: relative;
}

body.showEditorSelection .code-active-line:before,
body.showEditorSelection .code-line:hover:before {
	content: "";
	display: block;
	position: absolute;
	top: 0;
	left: -12px;
	height: 100%;
}

body.showEditorSelection li.code-active-line:before,
body.showEditorSelection li.code-line:hover:before {
	left: -30px;
}

.vscode-light.showEditorSelection .code-active-line:before {
	border-left: 3px solid rgba(0, 0, 0, 0.15);
}

.vscode-light.showEditorSelection .code-line:hover:before {
	border-left: 3px solid rgba(0, 0, 0, 0.40);
}

.vscode-dark.showEditorSelection .code-active-line:before {
	border-left: 3px solid rgba(255, 255, 255, 0.4);
}

.vscode-dark.showEditorSelection .code-line:hover:before {
	border-left: 3px solid rgba(255, 255, 255, 0.60);
}

.vscode-high-contrast.showEditorSelection .code-active-line:before {
	border-left: 3px solid rgba(255, 160, 0, 0.7);
}

.vscode-high-contrast.showEditorSelection .code-line:hover:before {
	border-left: 3px solid rgba(255, 160, 0, 1);
}

img {
	max-width: 100%;
	max-height: 100%;
}

a {
	color: #4080D0;
	text-decoration: none;
}

a:focus,
input:focus,
select:focus,
textarea:focus {
	outline: 1px solid -webkit-focus-ring-color;
	outline-offset: -1px;
}

hr {
	border: 0;
	height: 2px;
	border-bottom: 2px solid;
}

h1 {
	padding-bottom: 0.3em;
	line-height: 1.2;
	border-bottom-width: 1px;
	border-bottom-style: solid;
}

h1, h2, h3 {
	font-weight: normal;
}

h1 code,
h2 code,
h3 code,
h4 code,
h5 code,
h6 code {
	font-size: inherit;
	line-height: auto;
}

a:hover {
	color: #4080D0;
	text-decoration: underline;
}

table {
	border-collapse: collapse;
}

table > thead > tr > th {
	text-align: left;
	border-bottom: 1px solid;
}

table > thead > tr > th,
table > thead > tr > td,
table > tbody > tr > th,
table > tbody > tr > td {
	padding: 5px 10px;
}

table > tbody > tr + tr > td {
	border-top: 1px solid;
}

blockquote {
	margin: 0 7px 0 5px;
	padding: 0 16px 0 10px;
	border-left: 5px solid;
}

code {
	font-family: Menlo, Monaco, Consolas, "Droid Sans Mono", "Courier New", monospace, "Droid Sans Fallback";
	font-size: 14px;
	line-height: 19px;
}

body.wordWrap pre {
	white-space: pre-wrap;
}

.mac code {
	font-size: 12px;
	line-height: 18px;
}

pre:not(.hljs),
pre.hljs code > div {
	padding: 16px;
	border-radius: 3px;
	overflow: auto;
}

/** Theming */

.vscode-light,
.vscode-light pre code {
	color: rgb(30, 30, 30);
}

.vscode-dark,
.vscode-dark pre code {
	color: #DDD;
}

.vscode-high-contrast,
.vscode-high-contrast pre code {
	color: white;
}

.vscode-light code {
	color: #A31515;
}

.vscode-dark code {
	color: #D7BA7D;
}

.vscode-light pre:not(.hljs),
.vscode-light code > div {
	background-color: rgba(220, 220, 220, 0.4);
}

.vscode-dark pre:not(.hljs),
.vscode-dark code > div {
	background-color: rgba(10, 10, 10, 0.4);
}

.vscode-high-contrast pre:not(.hljs),
.vscode-high-contrast code > div {
	background-color: rgb(0, 0, 0);
}

.vscode-high-contrast h1 {
	border-color: rgb(0, 0, 0);
}

.vscode-light table > thead > tr > th {
	border-color: rgba(0, 0, 0, 0.69);
}

.vscode-dark table > thead > tr > th {
	border-color: rgba(255, 255, 255, 0.69);
}

.vscode-light h1,
.vscode-light hr,
.vscode-light table > tbody > tr + tr > td {
	border-color: rgba(0, 0, 0, 0.18);
}

.vscode-dark h1,
.vscode-dark hr,
.vscode-dark table > tbody > tr + tr > td {
	border-color: rgba(255, 255, 255, 0.18);
}

.vscode-light blockquote,
.vscode-dark blockquote {
	background: rgba(127, 127, 127, 0.1);
	border-color: rgba(0, 122, 204, 0.5);
}

.vscode-high-contrast blockquote {
	background: transparent;
	border-color: #fff;
}
</style>

<style>
/* Tomorrow Theme */
/* http://jmblog.github.com/color-themes-for-google-code-highlightjs */
/* Original theme - https://github.com/chriskempson/tomorrow-theme */

/* Tomorrow Comment */
.hljs-comment,
.hljs-quote {
	color: #8e908c;
}

/* Tomorrow Red */
.hljs-variable,
.hljs-template-variable,
.hljs-tag,
.hljs-name,
.hljs-selector-id,
.hljs-selector-class,
.hljs-regexp,
.hljs-deletion {
	color: #c82829;
}

/* Tomorrow Orange */
.hljs-number,
.hljs-built_in,
.hljs-builtin-name,
.hljs-literal,
.hljs-type,
.hljs-params,
.hljs-meta,
.hljs-link {
	color: #f5871f;
}

/* Tomorrow Yellow */
.hljs-attribute {
	color: #eab700;
}

/* Tomorrow Green */
.hljs-string,
.hljs-symbol,
.hljs-bullet,
.hljs-addition {
	color: #718c00;
}

/* Tomorrow Blue */
.hljs-title,
.hljs-section {
	color: #4271ae;
}

/* Tomorrow Purple */
.hljs-keyword,
.hljs-selector-tag {
	color: #8959a8;
}

.hljs {
	display: block;
	overflow-x: auto;
	color: #4d4d4c;
	padding: 0.5em;
}

.hljs-emphasis {
	font-style: italic;
}

.hljs-strong {
	font-weight: bold;
}
</style>

<style>
/*
 * Markdown PDF CSS
 */

 body {
	font-family:  "Meiryo", "Segoe WPC", "Segoe UI", "SFUIText-Light", "HelveticaNeue-Light", sans-serif, "Droid Sans Fallback";
}

pre {
	background-color: #f8f8f8;
	border: 1px solid #cccccc;
	border-radius: 3px;
	overflow-x: auto;
	white-space: pre-wrap;
	overflow-wrap: break-word;
}

pre:not(.hljs) {
	padding: 23px;
	line-height: 19px;
}

blockquote {
	background: rgba(127, 127, 127, 0.1);
	border-color: rgba(0, 122, 204, 0.5);
}

.emoji {
	height: 1.4em;
}

/* for inline code */
:not(pre):not(.hljs) > code {
	color: #C9AE75; /* Change the old color so it seems less like an error */
	font-size: inherit;
}

/* Page Break : use <div class="page"/> to insert page break
-------------------------------------------------------- */
.page {
	page-break-after: always;
}

</style>

</head>
<body>
<!-- <script type="text/javascript" src="MathJax.js"></script> -->
<h1 id="kerberos%E6%8E%A5%E5%8F%A3%E6%96%87%E6%A1%A3">Kerberos接口文档</h1>
<h2 id="%E4%B8%80%E3%80%81%E7%94%A8%E6%88%B7-as%E8%AE%A4%E8%AF%81%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%8E%A5%E5%8F%A3%EF%BC%88c-as%EF%BC%89">一、用户-AS认证服务器接口（C-AS）</h2>
<h3 id="1-%E6%B3%A8%E5%86%8C%E6%9C%8D%E5%8A%A1">1. 注册服务</h3>
<ol>
<li><strong>接口说明</strong></li>
</ol>
<table>
<thead>
<tr>
<th style="text-align:center">接口简介</th>
<th style="text-align:center">请求地址</th>
<th style="text-align:center">请求类型</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">管理用户注册的用户名，密码，并返回用户-AS认证服务器（C-AS）的共享密钥生成参数salt,以及加密类型</td>
<td style="text-align:center">http://ip/kerberosService/api</td>
<td style="text-align:center">POST</td>
</tr>
</tbody>
</table>
<ol start="2">
<li><strong>请求参数</strong></li>
</ol>
<table>
<thead>
<tr>
<th>参数名</th>
<th style="text-align:center">必填</th>
<th style="text-align:center">类型</th>
<th style="text-align:center">描述</th>
</tr>
</thead>
<tbody>
<tr>
<td>user</td>
<td style="text-align:center">是</td>
<td style="text-align:center">string</td>
<td style="text-align:center">用户名</td>
</tr>
<tr>
<td>password</td>
<td style="text-align:center">是</td>
<td style="text-align:center">string</td>
<td style="text-align:center">用户密码(SHA256 哈希值)</td>
</tr>
</tbody>
</table>
<p>请求示例:</p>
<pre class="hljs"><code><div>    {
        <span class="hljs-attr">"type"</span>: <span class="hljs-string">"register"</span>,
        <span class="hljs-attr">"data"</span>:{
            <span class="hljs-attr">"user"</span>: <span class="hljs-string">"test401"</span>,
            <span class="hljs-attr">"password"</span>: <span class="hljs-string">"flkaj932pj2230920923fadfasdfasdfoasd"</span>
        }
    }
</div></code></pre>
<ol start="3">
<li><strong>返回数据示例</strong></li>
</ol>
<pre class="hljs"><code><div>    // 注册成功
    {
        <span class="hljs-attr">"data"</span>:{
            // 注册状态
            <span class="hljs-attr">"status"</span>: <span class="hljs-string">"success"</span>,
            // 共享密钥生成参数
            <span class="hljs-attr">"salt"</span>: <span class="hljs-string">"565989"</span>,
            // 加密类型
            <span class="hljs-attr">"crptyo_type"</span>: <span class="hljs-string">"RC4"</span>
        }
    }
    // 注册失败
    {
        <span class="hljs-attr">"data"</span>:{
            // 注册状态
            <span class="hljs-attr">"status"</span>: <span class="hljs-string">"false"</span>,
            // 失败原因 <span class="hljs-attr">"0:用户名已存在"</span>
            <span class="hljs-attr">"reason"</span>: <span class="hljs-string">"0"</span>
        }
    }
</div></code></pre>
<p>加密算法列表:</p>
<pre class="hljs"><code><div>    // 加密算法
    RC<span class="hljs-number">4</span>, <span class="hljs-number">3</span>DES, AES
    // 哈希算法
    MD<span class="hljs-number">5</span>, SHA<span class="hljs-number">1</span>, SHA<span class="hljs-number">2</span>, SHA<span class="hljs-number">2</span><span class="hljs-number">5</span><span class="hljs-number">6</span>
</div></code></pre>
<h3 id="2-%E4%BF%AE%E6%94%B9%E5%AF%86%E7%A0%81">2. 修改密码</h3>
<table>
<thead>
<tr>
<th style="text-align:center">接口简介</th>
<th style="text-align:center">请求地址</th>
<th style="text-align:center">请求类型</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">更新用户密码, 返回(新)用户-AS认证服务器（C-AS）的共享密钥生成参数salt, 和加密类型</td>
<td style="text-align:center">http://ip/kerberosService/api</td>
<td style="text-align:center">POST</td>
</tr>
</tbody>
</table>
<ol start="2">
<li><strong>请求参数</strong></li>
</ol>
<table>
<thead>
<tr>
<th>参数名</th>
<th style="text-align:center">必填</th>
<th style="text-align:center">类型</th>
<th style="text-align:center">描述</th>
</tr>
</thead>
<tbody>
<tr>
<td>user</td>
<td style="text-align:center">是</td>
<td style="text-align:center">string</td>
<td style="text-align:center">用户名</td>
</tr>
<tr>
<td>ori_password</td>
<td style="text-align:center">是</td>
<td style="text-align:center">string</td>
<td style="text-align:center">用户密码(旧 SHA256)</td>
</tr>
<tr>
<td>new_password</td>
<td style="text-align:center">是</td>
<td style="text-align:center">string</td>
<td style="text-align:center">用户密码(新 SHA256)</td>
</tr>
</tbody>
</table>
<p>请求示例:</p>
<pre class="hljs"><code><div>    {
        <span class="hljs-attr">"type"</span>: <span class="hljs-string">"figure_password"</span>,
        <span class="hljs-attr">"data"</span>:{
            <span class="hljs-attr">"user"</span>: <span class="hljs-string">"test401"</span>,
            <span class="hljs-attr">"ori_password"</span>: <span class="hljs-string">"flkaj932pj2230920923fadfasdfasdfoasd"</span>,
            <span class="hljs-attr">"new_password"</span>: <span class="hljs-string">"flkaj932pj2230920923fadfasdfasdfo5d"</span>
        }
    }
</div></code></pre>
<ol start="3">
<li><strong>返回数据示例</strong></li>
</ol>
<pre class="hljs"><code><div>    // 修改密码成功
    {
        <span class="hljs-attr">"data"</span>:{
            // 修改状态
            <span class="hljs-attr">"status"</span>: <span class="hljs-string">"success"</span>,
            // (新)共享密钥生成参数
            <span class="hljs-attr">"salt"</span>: <span class="hljs-string">"989348"</span>,
            // 加密类型
            <span class="hljs-attr">"crptyo_type"</span>: <span class="hljs-string">"RC4"</span>
        }
    }
    // 注册失败
    {
        <span class="hljs-attr">"data"</span>:{
            // 修改状态
            <span class="hljs-attr">"status"</span>: <span class="hljs-string">"false"</span>,
            // 失败原因 <span class="hljs-attr">"0: 用户名不存在，1: 原始密码错误"</span>
            <span class="hljs-attr">"reason"</span>: <span class="hljs-string">"0/1"</span>
        }
    }
</div></code></pre>
<h3 id="3-%E7%94%B3%E8%AF%B7tgt%E7%A5%A8%E6%8D%AE">3. 申请TGT票据</h3>
<ol>
<li><strong>接口说明</strong></li>
</ol>
<table>
<thead>
<tr>
<th style="text-align:center">接口简介</th>
<th style="text-align:center">请求地址</th>
<th style="text-align:center">请求类型</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">用户向AS申请TGT票据ticket_tgs，返回加密数据(用C-AS的共享密钥Kc加密)</td>
<td style="text-align:center">http://ip/kerberosService/api</td>
<td style="text-align:center">POST</td>
</tr>
</tbody>
</table>
<ol start="2">
<li><strong>请求参数</strong></li>
</ol>
<table>
<thead>
<tr>
<th>参数名</th>
<th style="text-align:center">必填</th>
<th style="text-align:center">类型</th>
<th style="text-align:center">描述</th>
</tr>
</thead>
<tbody>
<tr>
<td>IDc</td>
<td style="text-align:center">是</td>
<td style="text-align:center">string</td>
<td style="text-align:center">用户名</td>
</tr>
<tr>
<td>IDtgs</td>
<td style="text-align:center">是</td>
<td style="text-align:center">string</td>
<td style="text-align:center">TGS服务器id：&quot;0&quot;</td>
</tr>
<tr>
<td>TS1</td>
<td style="text-align:center">是</td>
<td style="text-align:center">string</td>
<td style="text-align:center">当前时间戳</td>
</tr>
</tbody>
</table>
<p>请求示例:</p>
<pre class="hljs"><code><div>    {
        <span class="hljs-attr">"type"</span>: <span class="hljs-string">"request_tgt"</span>,
        <span class="hljs-attr">"data"</span>:{
            <span class="hljs-attr">"IDc"</span>: <span class="hljs-string">"user1"</span>,
            <span class="hljs-attr">"IDtgs"</span>: <span class="hljs-string">"0"</span>,
            <span class="hljs-attr">"TS1"</span>: <span class="hljs-string">"2019-07-29 08:24:56"</span>
        }
    }
</div></code></pre>
<ol start="3">
<li><strong>返回数据示例</strong></li>
</ol>
<pre class="hljs"><code><div>    //申请TGT成功
    {
        <span class="hljs-attr">"data"</span>:{
            // 申请状态
            <span class="hljs-attr">"status"</span>: <span class="hljs-string">"success"</span>,
            // 使用C-AS共享密钥Kc加密的数据; []表示加密
            // Kc[C-TGS共享密钥Kctgs, IDtgs, TS2, lifetime2, ticket_tgs]
            // ticket_tgs=Ktgs[Kctgs, IDc, IDtgs, TS2, lifetime2]
            <span class="hljs-attr">"encrypt"</span>:<span class="hljs-string">"flkaj932pj2230920923"</span>,
            // 加密类型
            <span class="hljs-attr">"crptyo_type"</span>: <span class="hljs-string">"RC4"</span>
        }
    }
    // 申请失败失败
    {
        <span class="hljs-attr">"data"</span>:{
            // 注册状态
            <span class="hljs-attr">"status"</span>: <span class="hljs-string">"false"</span>,
            // 失败原因 <span class="hljs-attr">"0: 用户名不存在; 1: 密码错误"</span>
            <span class="hljs-attr">"reason"</span>: <span class="hljs-string">"0/1"</span>
        }
    }
</div></code></pre>
<h2 id="%E4%BA%8C%E3%80%81%E7%94%A8%E6%88%B7-tgs%E7%A5%A8%E6%8D%AE%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%8E%A5%E5%8F%A3%EF%BC%88c-tgs%EF%BC%89">二、用户-TGS票据服务器接口（C-TGS）</h2>
<h3 id="1-%E5%90%91tgs%E8%AF%B7%E6%B1%82%E7%A5%A8%E6%8D%AE">1. 向TGS请求票据</h3>
<ol>
<li><strong>接口说明</strong></li>
</ol>
<table>
<thead>
<tr>
<th style="text-align:center">接口简介</th>
<th style="text-align:center">请求地址</th>
<th style="text-align:center">请求类型</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">用户向TGS申请票据ticket_v，返回加密数据(用C-AS的共享密钥Kc加密)</td>
<td style="text-align:center">http://ip/kerberosService/api</td>
<td style="text-align:center">POST</td>
</tr>
</tbody>
</table>
<ol start="2">
<li><strong>请求参数</strong></li>
</ol>
<table>
<thead>
<tr>
<th>参数名</th>
<th style="text-align:center">必填</th>
<th style="text-align:center">类型</th>
<th style="text-align:center">描述</th>
</tr>
</thead>
<tbody>
<tr>
<td>IDo</td>
<td style="text-align:center">是</td>
<td style="text-align:center">string</td>
<td style="text-align:center">版权方id</td>
</tr>
<tr>
<td>IDv</td>
<td style="text-align:center">是</td>
<td style="text-align:center">string</td>
<td style="text-align:center">访问Hadoop云服务器id(&quot;0&quot;)</td>
</tr>
<tr>
<td>ticket_tgs</td>
<td style="text-align:center">是</td>
<td style="text-align:center">string</td>
<td style="text-align:center">TGS票据(用户从AS返回的加密数据解密结果)</td>
</tr>
<tr>
<td>auth</td>
<td style="text-align:center">是</td>
<td style="text-align:center">string</td>
<td style="text-align:center">用户身份证明信息</td>
</tr>
</tbody>
</table>
<p>请求参数示例:</p>
<pre class="hljs"><code><div>    // []表示加密
    auth=Kctgs[IDc, IDo, TS3]
</div></code></pre>
<p>请求示例:</p>
<pre class="hljs"><code><div>    {
        <span class="hljs-attr">"type"</span>: <span class="hljs-string">"request_tgt"</span>,
        <span class="hljs-attr">"data"</span>:{
            <span class="hljs-attr">"IDo"</span>: <span class="hljs-string">"bilibili"</span>,
            <span class="hljs-attr">"IDv"</span>: <span class="hljs-string">"0"</span>,
            <span class="hljs-attr">"ticket_tgs"</span>: <span class="hljs-string">"56464dafj9389554fdasdsadfaadfasdfasdfoasd"</span>,
            <span class="hljs-attr">"auth"</span>: <span class="hljs-string">"5dhfaodif8953645sadfaadfasdfasdfoasd"</span>
        }
    }
</div></code></pre>
<ol start="3">
<li><strong>返回数据示例</strong></li>
</ol>
<pre class="hljs"><code><div>    // 申请成功
    {
        <span class="hljs-attr">"data"</span>:{
            // 申请状态
            <span class="hljs-attr">"status"</span>: <span class="hljs-string">"success"</span>,
            // 使用C-TGS共享密钥Kctgs加密的数据; []表示加密
            // Kctgs[C-V共享密钥Kcv, IDo, IDv, TS4, ticket_v]
            // ticket_v=Kv[Kcv, IDc, IDo, IDv, TS4, lifetime4, AC_c] 
            <span class="hljs-attr">"encrypt"</span>: <span class="hljs-string">"flkaj932pj2230920923"</span>,
            <span class="hljs-attr">"type"</span>: <span class="hljs-string">"RC4"</span>
        }
    }
    // 申请失败
    {
        <span class="hljs-attr">"data"</span>:{
            // 申请状态
            <span class="hljs-attr">"status"</span>: <span class="hljs-string">"false"</span>,
            // 失败原因 <span class="hljs-attr">"0: 用户验证失败"</span>
            <span class="hljs-attr">"reason"</span>: <span class="hljs-string">"0"</span>
        }
    }
</div></code></pre>
<h2 id="%E4%B8%89%E3%80%81kerberos%E7%AE%A1%E7%90%86%E5%8A%9F%E8%83%BD">三、Kerberos管理功能</h2>
<h3 id="1-%E8%AE%BE%E7%BD%AE%E7%A5%A8%E6%8D%AE%E6%9C%89%E6%95%88%E6%9C%9F">1. 设置票据有效期</h3>
<ol>
<li><strong>接口说明</strong></li>
</ol>
<table>
<thead>
<tr>
<th style="text-align:center">接口简介</th>
<th style="text-align:center">请求地址</th>
<th style="text-align:center">请求类型</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">kerberos管理员设置票据有效期</td>
<td style="text-align:center">http://ip/kerberosService/api</td>
<td style="text-align:center">POST</td>
</tr>
</tbody>
</table>
<ol start="2">
<li><strong>请求参数</strong></li>
</ol>
<table>
<thead>
<tr>
<th>参数名</th>
<th style="text-align:center">必填</th>
<th style="text-align:center">类型</th>
<th style="text-align:center">描述</th>
</tr>
</thead>
<tbody>
<tr>
<td>user</td>
<td style="text-align:center">是</td>
<td style="text-align:center">string</td>
<td style="text-align:center">管理员用户名</td>
</tr>
<tr>
<td>password</td>
<td style="text-align:center">是</td>
<td style="text-align:center">string</td>
<td style="text-align:center">管理员密码(SHA256)</td>
</tr>
<tr>
<td>lifetime</td>
<td style="text-align:center">是</td>
<td style="text-align:center">string</td>
<td style="text-align:center">票据有效期</td>
</tr>
</tbody>
</table>
<p>请求示例:</p>
<pre class="hljs"><code><div>    {
        <span class="hljs-attr">"type"</span>: <span class="hljs-string">"figure_lifetime"</span>,
        <span class="hljs-attr">"data"</span>:{
            <span class="hljs-attr">"user"</span>: <span class="hljs-string">"admin"</span>,
            <span class="hljs-attr">"password"</span>: <span class="hljs-string">"56464dafj9389554fdasdsadfaadfasdfasdfoasd"</span>,
            <span class="hljs-attr">"lifetime"</span>: <span class="hljs-string">"564652"</span>
        }
    }
</div></code></pre>
<ol start="3">
<li><strong>返回数据示例</strong></li>
</ol>
<pre class="hljs"><code><div>    // 设置成功
    {
        <span class="hljs-attr">"data"</span>:{
            // 设置状态
            <span class="hljs-attr">"status"</span>: <span class="hljs-string">"success"</span>
        }
    }
    // 设置失败
    {
        <span class="hljs-attr">"data"</span>:{
            // 设置状态
            <span class="hljs-attr">"status"</span>: <span class="hljs-string">"false"</span>,
            // 失败原因 <span class="hljs-attr">"0: 用户验证失败，1: 系统错误"</span>
            <span class="hljs-attr">"reason"</span>: <span class="hljs-string">"0/1"</span>
        }
    }
</div></code></pre>
<h3 id="2-%E8%AE%BE%E7%BD%AE%E5%8A%A0%E5%AF%86%E7%AE%97%E6%B3%95">2. 设置加密算法</h3>
<ol>
<li><strong>接口说明</strong></li>
</ol>
<table>
<thead>
<tr>
<th style="text-align:center">接口简介</th>
<th style="text-align:center">请求地址</th>
<th style="text-align:center">请求类型</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">kerberos管理员设置使用的加密算法</td>
<td style="text-align:center">http://ip/kerberosService/api</td>
<td style="text-align:center">POST</td>
</tr>
</tbody>
</table>
<ol start="2">
<li><strong>请求参数</strong></li>
</ol>
<table>
<thead>
<tr>
<th>参数名</th>
<th style="text-align:center">必填</th>
<th style="text-align:center">类型</th>
<th style="text-align:center">描述</th>
</tr>
</thead>
<tbody>
<tr>
<td>user</td>
<td style="text-align:center">是</td>
<td style="text-align:center">string</td>
<td style="text-align:center">管理员用户名</td>
</tr>
<tr>
<td>password</td>
<td style="text-align:center">是</td>
<td style="text-align:center">string</td>
<td style="text-align:center">管理员密码(SHA256)</td>
</tr>
<tr>
<td>crypto_type</td>
<td style="text-align:center">是</td>
<td style="text-align:center">string</td>
<td style="text-align:center">加密算法</td>
</tr>
</tbody>
</table>
<p>加密算法列表:</p>
<pre class="hljs"><code><div>    // 加密算法
    RC<span class="hljs-number">4</span>, <span class="hljs-number">3</span>DES, AES
    // 哈希算法
    MD<span class="hljs-number">5</span>, SHA<span class="hljs-number">1</span>, SHA<span class="hljs-number">2</span>, SHA<span class="hljs-number">2</span><span class="hljs-number">5</span><span class="hljs-number">6</span>
</div></code></pre>
<p>请求示例:</p>
<pre class="hljs"><code><div>    {
        <span class="hljs-attr">"type"</span>: <span class="hljs-string">"figure_crypto"</span>,
        <span class="hljs-attr">"data"</span>:{
            <span class="hljs-attr">"user"</span>: <span class="hljs-string">"admin"</span>,
            <span class="hljs-attr">"password"</span>: <span class="hljs-string">"56464dafj9389554fdasdsadfaadfasdfasdfoasd"</span>,
            <span class="hljs-attr">"crypto_type"</span>: <span class="hljs-string">"RC4"</span>
        }
    }
</div></code></pre>
<ol start="3">
<li><strong>返回数据示例</strong></li>
</ol>
<pre class="hljs"><code><div>    // 设置成功
    {
        <span class="hljs-attr">"data"</span>:{
            // 设置状态
            <span class="hljs-attr">"status"</span>: <span class="hljs-string">"success"</span>
        }
    }
    // 设置失败
    {
        <span class="hljs-attr">"data"</span>:{
            // 设置状态
            <span class="hljs-attr">"status"</span>: <span class="hljs-string">"false"</span>,
            // 失败原因 <span class="hljs-attr">"0: 用户验证失败，1: 系统错误"</span>
            <span class="hljs-attr">"reason"</span>: <span class="hljs-string">"0/1"</span>
        }
    }
</div></code></pre>
<!-- 票据有效期
加密算法和hash算法设置 -->
<h2 id="%E5%9B%9B%E3%80%81kerberos-blockchain%E6%8E%A5%E5%8F%A3">四、Kerberos-Blockchain接口</h2>
<p>###1. 记录票据接口</p>
<pre class="hljs"><code><div>    {
        <span class="hljs-attr">"key"</span>: <span class="hljs-string">"IDc||IDo"</span>,
        <span class="hljs-attr">"value"</span>:{
            <span class="hljs-attr">"encrypted_value"</span>: <span class="hljs-string">"flkaj932pj2230920923fadfasdfasdfoasd"</span>,
            <span class="hljs-attr">"lifetime"</span>: <span class="hljs-string">"562694"</span>,
        }
    }
</div></code></pre>
<h2 id="%E4%BA%94%E3%80%81hadoop%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8-kerberos%E8%AE%A4%E8%AF%81%E6%9C%8D%E5%8A%A1%E5%8D%8F%E8%AE%AE">五、Hadoop云服务器-Kerberos认证服务协议</h2>
<ol>
<li><strong>协议说明</strong></li>
</ol>
<p>协议简介Hadoop认证Kerberos提供的票据信息的标准。</p>
<ol start="2">
<li><strong>请求参数</strong></li>
</ol>
<table>
<thead>
<tr>
<th>参数名称</th>
<th style="text-align:center">是否必须</th>
<th style="text-align:center">类型</th>
<th style="text-align:center">描述</th>
</tr>
</thead>
<tbody>
<tr>
<td>Ticket_v</td>
<td style="text-align:center">必须</td>
<td style="text-align:center">object</td>
<td style="text-align:center">用户用于访问Hadoop云存储服务器的ticket信息（从TGS服务器获取）</td>
</tr>
<tr>
<td>Authenticator_c</td>
<td style="text-align:center">必须</td>
<td style="text-align:center">object</td>
<td style="text-align:center">标识用户身份信息（使用用户与服务器的共享密钥加密）</td>
</tr>
</tbody>
</table>
<ol start="3">
<li>
<p><strong>参数特殊说明</strong></p>
<ol>
<li>
<p>参数含义</p>
<p>Ticket_v$=E_{K_v}[K_{c,v}||ID_c||ID_o||ID_v||TS_4||lifetime_4||AC_c]$</p>
<p>Authenticator_c$=E_{K_{c,v}}[ID_c||ID_o||ID_v||TS_5]$</p>
<p>$K_v$: TGS和云服务器的共享密钥</p>
<p>$K_{c,v}$: 客户端和云服务器的共享密钥</p>
<p>$ID_c$: 用户身份信息标识</p>
<p>$ID_o$: 请求专利信息标识</p>
<p>$ID_v$: 请求云服务器标识（系统中目前只有一个Hadoop服务器）</p>
<p>$TS_i$: 时间戳</p>
<p>$lifetime_i$: 活动时间长度</p>
<p>$AC_c$: 访问控制单元</p>
</li>
<li>
<p>特别参数格式说明(AC_c，目前给出两种方式)</p>
<pre class="hljs"><code><div>AC_c={
    // 用户C的身份ID
    user_id: id_c,
    // 权限信息
    permission: {
        // 用户C持有的版权所有方O_i的权限信息（文件夹）
        id_o1: {
            // 版权所有方O_i的版权文件编标识
            // 用户C都对此版权文件的权限信息（读/下载/禁止）
            id_o1_permission: read/download/prohibit,
            id_o11: read/download/prohibit,
            id_o12: read/download/prohibit,
        },
        id_o2: {
            id_o21: read/download/prohibit,
            id_o22: read/download/prohibit,
        },
    }
}
</div></code></pre>
</li>
</ol>
</li>
</ol>

</body>
</html>
