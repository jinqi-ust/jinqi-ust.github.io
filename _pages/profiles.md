---
layout: page
title: People
permalink: /people/
nav: true
nav_order: 5
---

<style>
.people-section {
  margin-bottom: 2.4rem;
}

.people-section h2 {
  color: #1e88e5;
  font-weight: 400;
  font-size: 1.55rem;
  margin-bottom: 1.1rem;
  line-height: 1.2;
}

.person-row {
  margin-bottom: 1.6rem;
}

.person-info h3 {
  margin: 0 0 0.22rem 0;
  font-size: 1.35rem;
  font-weight: 400;
  line-height: 1.2;
}

.person-role {
  font-style: italic;
  font-size: 1.02rem;
  margin-bottom: 0.22rem;
  line-height: 1.35;
}

.person-affiliation {
  font-size: 0.98rem;
  margin-bottom: 0.22rem;
  line-height: 1.45;
}

.person-placement {
  font-size: 0.98rem;
  margin-bottom: 0.22rem;
  line-height: 1.45;
  color: #555;
}
</style>

<div class="people-section">
  <h2>Principal Investigator</h2>
  {% for person in site.data.people.principal_investigator %}
    <div class="person-row">
      <div class="person-info">
        <h3>{{ person.name }}</h3>
        <div class="person-role">{{ person.role }}</div>
        {% if person.affiliation %}
          <div class="person-affiliation">{{ person.affiliation }}</div>
        {% endif %}
      </div>
    </div>
  {% endfor %}
</div>

<div class="people-section">
  <h2>Current Students</h2>
  {% for person in site.data.people.Current_Students %}
    <div class="person-row">
      <div class="person-info">
        <h3>{{ person.name }}</h3>
        <div class="person-role">{{ person.role }}</div>
        {% if person.affiliation %}
          <div class="person-affiliation">{{ person.affiliation }}</div>
        {% endif %}
      </div>
    </div>
  {% endfor %}
</div>

<div class="people-section">
  <h2>Graduated Students</h2>
  {% for person in site.data.people.Graduated_Students %}
    <div class="person-row">
      <div class="person-info">
        <h3>{{ person.name }}</h3>
        <div class="person-role">{{ person.role }}</div>
        {% if person.affiliation %}
          <div class="person-affiliation">{{ person.affiliation }}</div>
        {% endif %}
        {% if person.placement %}
          <div class="person-placement">{{ person.placement }}</div>
        {% endif %}
      </div>
    </div>
  {% endfor %}
</div>
