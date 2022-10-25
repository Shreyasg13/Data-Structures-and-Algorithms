<h2><a href="https://leetcode.com/problems/unique-email-addresses/">929. Unique Email Addresses</a></h2><h3>Easy</h3><hr><div><p><nr-sentence class="nr-s0" id="nr-s0" page="0">Every </nr-sentence><strong><nr-sentence class="nr-s0" id="nr-s0" page="0">valid email</nr-sentence></strong><nr-sentence class="nr-s0" id="nr-s0" page="0"> consists of a </nr-sentence><strong><nr-sentence class="nr-s0" id="nr-s0" page="0">local name</nr-sentence></strong><nr-sentence class="nr-s0" id="nr-s0" page="0"> and a </nr-sentence><strong><nr-sentence class="nr-s0" id="nr-s0" page="0">domain name</nr-sentence></strong><nr-sentence class="nr-s0" id="nr-s0" page="0">, separated by the </nr-sentence><code><nr-sentence class="nr-s0" id="nr-s0" page="0">'@'</nr-sentence></code><nr-sentence class="nr-s0" id="nr-s0" page="0"> sign.</nr-sentence><nr-sentence class="nr-s1" id="nr-s1" page="0"> Besides lowercase letters, the email may contain one or more </nr-sentence><code><nr-sentence class="nr-s1" id="nr-s1" page="0">'.'</nr-sentence></code><nr-sentence class="nr-s1" id="nr-s1" page="0"> or </nr-sentence><code><nr-sentence class="nr-s1" id="nr-s1" page="0">'+'</nr-sentence></code>.</p>

<ul>
	<li><nr-sentence class="nr-s2" id="nr-s2" page="0">For example, in </nr-sentence><code><nr-sentence class="nr-s2" id="nr-s2" page="0">"alice@leetcode.com"</nr-sentence></code><nr-sentence class="nr-s2" id="nr-s2" page="0">, </nr-sentence><code><nr-sentence class="nr-s2" id="nr-s2" page="0">"alice"</nr-sentence></code><nr-sentence class="nr-s2" id="nr-s2" page="0"> is the </nr-sentence><strong><nr-sentence class="nr-s2" id="nr-s2" page="0">local name</nr-sentence></strong><nr-sentence class="nr-s2" id="nr-s2" page="0">, and </nr-sentence><code><nr-sentence class="nr-s2" id="nr-s2" page="0">"leetcode.com"</nr-sentence></code><nr-sentence class="nr-s2" id="nr-s2" page="0"> is the </nr-sentence><strong><nr-sentence class="nr-s2" id="nr-s2" page="0">domain name</nr-sentence></strong><nr-sentence class="nr-s2" id="nr-s2" page="0">.</nr-sentence></li>
</ul>

<p><nr-sentence class="nr-s3" id="nr-s3" page="0">If you add periods </nr-sentence><code><nr-sentence class="nr-s3" id="nr-s3" page="0">'.'</nr-sentence></code><nr-sentence class="nr-s3" id="nr-s3" page="0"> between some characters in the </nr-sentence><strong><nr-sentence class="nr-s3" id="nr-s3" page="0">local name</nr-sentence></strong><nr-sentence class="nr-s3" id="nr-s3" page="0"> part of an email address, mail sent there will be forwarded to the same address without dots in the local name.</nr-sentence><nr-sentence class="nr-s4" id="nr-s4" page="0"> Note that this rule </nr-sentence><strong><nr-sentence class="nr-s4" id="nr-s4" page="0">does not apply</nr-sentence></strong><nr-sentence class="nr-s4" id="nr-s4" page="0"> to </nr-sentence><strong><nr-sentence class="nr-s4" id="nr-s4" page="0">domain names</nr-sentence></strong>.</p>

<ul>
	<li><nr-sentence class="nr-s5" id="nr-s5" page="0">For example, </nr-sentence><code><nr-sentence class="nr-s5" id="nr-s5" page="0">"alice.z@leetcode.com"</nr-sentence></code><nr-sentence class="nr-s5" id="nr-s5" page="0"> and </nr-sentence><code><nr-sentence class="nr-s5" id="nr-s5" page="0">"alicez@leetcode.com"</nr-sentence></code><nr-sentence class="nr-s5" id="nr-s5" page="0"> forward to the same email address.</nr-sentence></li>
</ul>

<p><nr-sentence class="nr-s6" id="nr-s6" page="0">If you add a plus </nr-sentence><code><nr-sentence class="nr-s6" id="nr-s6" page="0">'+'</nr-sentence></code><nr-sentence class="nr-s6" id="nr-s6" page="0"> in the </nr-sentence><strong><nr-sentence class="nr-s6" id="nr-s6" page="0">local name</nr-sentence></strong><nr-sentence class="nr-s6" id="nr-s6" page="0">, everything after the first plus sign </nr-sentence><strong><nr-sentence class="nr-s6" id="nr-s6" page="0">will be ignored</nr-sentence></strong><nr-sentence class="nr-s6" id="nr-s6" page="0">.</nr-sentence><nr-sentence class="nr-s7" id="nr-s7" page="0"> This allows certain emails to be filtered.</nr-sentence><nr-sentence class="nr-s8" id="nr-s8" page="0"> Note that this rule </nr-sentence><strong><nr-sentence class="nr-s8" id="nr-s8" page="0">does not apply</nr-sentence></strong><nr-sentence class="nr-s8" id="nr-s8" page="0"> to </nr-sentence><strong><nr-sentence class="nr-s8" id="nr-s8" page="0">domain names</nr-sentence></strong>.</p>

<ul>
	<li><nr-sentence class="nr-s9" id="nr-s9" page="0">For example, </nr-sentence><code><nr-sentence class="nr-s9" id="nr-s9" page="0">"m.y+name@email.com"</nr-sentence></code><nr-sentence class="nr-s9" id="nr-s9" page="0"> will be forwarded to </nr-sentence><code><nr-sentence class="nr-s9" id="nr-s9" page="0">"my@email.com"</nr-sentence></code>.</li>
</ul>

<p><nr-sentence class="nr-s10" id="nr-s10" page="0">It is possible to use both of these rules at the same time.</nr-sentence></p>

<p><nr-sentence class="nr-s11" id="nr-s11" page="0">Given an array of strings </nr-sentence><code><nr-sentence class="nr-s11" id="nr-s11" page="0">emails</nr-sentence></code><nr-sentence class="nr-s11" id="nr-s11" page="0"> where we send one email to each </nr-sentence><code><nr-sentence class="nr-s11" id="nr-s11" page="0">emails[i]</nr-sentence></code><nr-sentence class="nr-s11" id="nr-s11" page="0">, return </nr-sentence><em><nr-sentence class="nr-s11" id="nr-s11" page="0">the number of different addresses that actually receive mails</nr-sentence></em><nr-sentence class="nr-s11" id="nr-s11" page="0">.</nr-sentence></p>

<p>&nbsp;</p>
<p><strong class="example"><nr-sentence class="nr-s12" id="nr-s12" page="0">Example 1:</nr-sentence></strong></p>

<pre><strong><nr-sentence class="nr-s13" id="nr-s13" page="0">Input:</nr-sentence></strong><nr-sentence class="nr-s13" id="nr-s13" page="0"> emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
</nr-sentence><strong><nr-sentence class="nr-s13" id="nr-s13" page="0">Output:</nr-sentence></strong><nr-sentence class="nr-s13" id="nr-s13" page="0"> 2
</nr-sentence><strong><nr-sentence class="nr-s13" id="nr-s13" page="0">Explanation:</nr-sentence></strong><nr-sentence class="nr-s13" id="nr-s13" page="0"> "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.</nr-sentence>
</pre>

<p><strong class="example"><nr-sentence class="nr-s14" id="nr-s14" page="0">Example 2:</nr-sentence></strong></p>

<pre><strong><nr-sentence class="nr-s15" id="nr-s15" page="0">Input:</nr-sentence></strong><nr-sentence class="nr-s15" id="nr-s15" page="0"> emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
</nr-sentence><strong><nr-sentence class="nr-s15" id="nr-s15" page="0">Output:</nr-sentence></strong><nr-sentence class="nr-s15" id="nr-s15" page="0"> 3</nr-sentence>
</pre>

<p>&nbsp;</p>
<p><strong><nr-sentence class="nr-s16" id="nr-s16" page="0">Constraints:</nr-sentence></strong></p>

<ul>
	<li><code><nr-sentence class="nr-s17" id="nr-s17" page="0">1 &lt;= emails.length &lt;= 100</nr-sentence></code></li>
	<li><code><nr-sentence class="nr-s18" id="nr-s18" page="0">1 &lt;= emails[i].length &lt;= 100</nr-sentence></code></li>
	<li><code><nr-sentence class="nr-s19" id="nr-s19" page="0">emails[i]</nr-sentence></code><nr-sentence class="nr-s19" id="nr-s19" page="0"> consist of lowercase English letters, </nr-sentence><code><nr-sentence class="nr-s19" id="nr-s19" page="0">'+'</nr-sentence></code><nr-sentence class="nr-s19" id="nr-s19" page="0">, </nr-sentence><code><nr-sentence class="nr-s19" id="nr-s19" page="0">'.'</nr-sentence></code><nr-sentence class="nr-s19" id="nr-s19" page="0"> and </nr-sentence><code><nr-sentence class="nr-s19" id="nr-s19" page="0">'@'</nr-sentence></code><nr-sentence class="nr-s19" id="nr-s19" page="0">.</nr-sentence></li>
	<li><nr-sentence class="nr-s20" id="nr-s20" page="0">Each </nr-sentence><code><nr-sentence class="nr-s20" id="nr-s20" page="0">emails[i]</nr-sentence></code><nr-sentence class="nr-s20" id="nr-s20" page="0"> contains exactly one </nr-sentence><code><nr-sentence class="nr-s20" id="nr-s20" page="0">'@'</nr-sentence></code><nr-sentence class="nr-s20" id="nr-s20" page="0"> character.</nr-sentence></li>
	<li><nr-sentence class="nr-s21" id="nr-s21" page="0">All local and domain names are non-empty.</nr-sentence></li>
	<li><nr-sentence class="nr-s22" id="nr-s22" page="0">Local names do not start with a </nr-sentence><code><nr-sentence class="nr-s22" id="nr-s22" page="0">'+'</nr-sentence></code><nr-sentence class="nr-s22" id="nr-s22" page="0"> character.</nr-sentence></li>
	<li><nr-sentence class="nr-s23" id="nr-s23" page="0">Domain names end with the </nr-sentence><code><nr-sentence class="nr-s23" id="nr-s23" page="0">".com"</nr-sentence></code><nr-sentence class="nr-s23" id="nr-s23" page="0"> suffix.</nr-sentence></li>
</ul>
</div>