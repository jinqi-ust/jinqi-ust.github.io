---
layout: page
title: people
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
  display: flex;
  align-items: flex-start;
  gap: 1.4rem;
  margin-bottom: 1.8rem;
}

.person-photo img {
  width: 200px;
  height: 200px;
  object-fit: cover;
  border-radius: 16px;
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
  margin-bottom: 0.75rem;
  line-height: 1.45;
}

.person-links a {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  margin-right: 0.45rem;
  border-radius: 8px;
  background: #000;
  color: #fff;
  text-decoration: none;
  font-size: 0.95rem;
}
</style>

<div class="people-section">
  <h2>Principal Investigator</h2>
  {% for person in site.data.people.principal_investigator %}
    <div class="person-row">
      <div class="person-photo">
        <img src="{{ '/assets/img/' | append: person.image | relative_url }}" alt="{{ person.name }}">
      </div>
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
  {% for person in site.data.people.Current_Students%}
    <div class="person-row">
      <div class="person-photo">
        <img src="{{ '/assets/img/' | append: person.image | relative_url }}" alt="{{ person.name }}">
      </div>
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
  {% for person in site.data.people.Graduated_Students%}
    <div class="person-row">
      <div class="person-photo">
        <img src="{{ '/assets/img/' | append: person.image | relative_url }}" alt="{{ person.name }}">
      </div>
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
