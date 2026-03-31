---
layout: page
title: people
permalink: /people/
nav: true
nav_order: 4
---

<style>
.people-section {
  margin-bottom: 3rem;
}
.people-section h2 {
  color: #1e88e5;
  font-weight: 700;
  margin-bottom: 1.5rem;
}
.person-row {
  display: flex;
  align-items: flex-start;
  gap: 2rem;
  margin-bottom: 2.5rem;
}
.person-photo img {
  width: 190px;
  height: 190px;
  object-fit: cover;
  border-radius: 18px;
}
.person-info h3 {
  margin: 0 0 0.4rem 0;
  font-size: 2.2rem;
  font-weight: 700;
}
.person-role {
  font-style: italic;
  font-size: 1.4rem;
  margin-bottom: 0.4rem;
}
.person-affiliation {
  font-size: 1.2rem;
  margin-bottom: 1rem;
}
.person-links a {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 42px;
  height: 42px;
  margin-right: 0.6rem;
  border-radius: 8px;
  background: #000;
  color: #fff;
  text-decoration: none;
  font-size: 1.2rem;
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
  <h2>Current Research Postgraduate Supervision:</h2>
  {% for person in site.data.people.Current Research Postgraduate Supervision: %}
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
  <h2>Graduated Research Postgraduate Supervision:</h2>
  {% for person in site.data.people.Graduated Research Postgraduate Supervision:%}
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
