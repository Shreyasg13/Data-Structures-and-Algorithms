<h2><a href="https://leetcode.com/problems/top-k-frequent-elements/">347. Top K Frequent Elements</a></h2><h3>Medium</h3><hr><div><p><nr-sentence class="nr-s0" id="nr-s0" page="0">Given an integer array </nr-sentence><code><nr-sentence class="nr-s0" id="nr-s0" page="0">nums</nr-sentence></code><nr-sentence class="nr-s0" id="nr-s0" page="0"> and an integer </nr-sentence><code><nr-sentence class="nr-s0" id="nr-s0" page="0">k</nr-sentence></code><nr-sentence class="nr-s0" id="nr-s0" page="0">, return </nr-sentence><em><nr-sentence class="nr-s0" id="nr-s0" page="0">the</nr-sentence></em> <code><nr-sentence class="nr-s0" id="nr-s0" page="0">k</nr-sentence></code> <em><nr-sentence class="nr-s0" id="nr-s0" page="0">most frequent elements</nr-sentence></em><nr-sentence class="nr-s1" id="nr-s1" page="0">. You may return the answer in </nr-sentence><strong><nr-sentence class="nr-s1" id="nr-s1" page="0">any order</nr-sentence></strong><nr-sentence class="nr-s1" id="nr-s1" page="0">.</nr-sentence></p>

<p>&nbsp;</p>
<p><strong><nr-sentence class="nr-s2" id="nr-s2" page="0">Example 1:</nr-sentence></strong></p>
<pre><strong><nr-sentence class="nr-s3" id="nr-s3" page="0">Input:</nr-sentence></strong><nr-sentence class="nr-s3" id="nr-s3" page="0"> nums = [1,1,1,2,2,3], k = 2
</nr-sentence><strong><nr-sentence class="nr-s3" id="nr-s3" page="0">Output:</nr-sentence></strong><nr-sentence class="nr-s3" id="nr-s3" page="0"> [1,2]</nr-sentence>
</pre><p><strong><nr-sentence class="nr-s4" id="nr-s4" page="0">Example 2:</nr-sentence></strong></p>
<pre><strong><nr-sentence class="nr-s5" id="nr-s5" page="0">Input:</nr-sentence></strong><nr-sentence class="nr-s5" id="nr-s5" page="0"> nums = [1], k = 1
</nr-sentence><strong><nr-sentence class="nr-s5" id="nr-s5" page="0">Output:</nr-sentence></strong><nr-sentence class="nr-s5" id="nr-s5" page="0"> [1]</nr-sentence>
</pre>
<p>&nbsp;</p>
<p><strong><nr-sentence class="nr-s6" id="nr-s6" page="0">Constraints:</nr-sentence></strong></p>

<ul>
	<li><code><nr-sentence class="nr-s7" id="nr-s7" page="0">1 &lt;= nums.length &lt;= 10</nr-sentence><sup style="">5</sup></code></li>
	<li><code><nr-sentence class="nr-s8" id="nr-s8" page="0">k</nr-sentence></code><nr-sentence class="nr-s8" id="nr-s8" page="0"> is in the range </nr-sentence><code><nr-sentence class="nr-s8" id="nr-s8" page="0">[1, the number of unique elements in the array]</nr-sentence></code>.</li>
	<li><nr-sentence class="nr-s9" id="nr-s9" page="0">It is </nr-sentence><strong><nr-sentence class="nr-s9" id="nr-s9" page="0">guaranteed</nr-sentence></strong><nr-sentence class="nr-s9" id="nr-s9" page="0"> that the answer is </nr-sentence><strong><nr-sentence class="nr-s9" id="nr-s9" page="0">unique</nr-sentence></strong>.</li>
</ul>

<p>&nbsp;</p>
<p><strong><nr-sentence class="nr-s10" id="nr-s10" page="0">Follow up:</nr-sentence></strong><nr-sentence class="nr-s10" id="nr-s10" page="0"> Your algorithm's time complexity must be better than </nr-sentence><code><nr-sentence class="nr-s10" id="nr-s10" page="0">O(n log n)</nr-sentence></code><nr-sentence class="nr-s10" id="nr-s10" page="0">, where n is the array's size.</nr-sentence></p>
</div>