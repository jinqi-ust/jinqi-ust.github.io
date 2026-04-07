---
layout: page
permalink: /publications/
title: Publications
nav: true
nav_order: 2
---

<!-- _pages/publications.md -->

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

<div class="publications">

<h2>Accepted</h2>
{% bibliography --query @*[note=Accepted] --sort-by year --order descending %}

<h2 style="margin-top: 2.5rem;">Under Review</h2>
{% bibliography --query @*[note=Under Review] %}

</div>


