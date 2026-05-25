---
permalink: /
layout: single
title: "About Me"
author_profile: true
---

## Hey, my name is Tomer
<div class="research-summary">
  <div>
    <p class="research-kicker">Ph.D. student in computer science</p>
    <p class="research-lead">I work at the intersection of differential privacy, statistics, and private data analysis, focusing on adapting classical statistical procedures to privacy constraints.</p>
  </div>
  <a class="cv-download" href="/files/Tomer_Shoham_CV.pdf" target="_blank" rel="noopener noreferrer">
    <i class="fas fa-file-arrow-down" aria-hidden="true"></i>
    Download CV
  </a>
</div>

I am a Ph.D. student in Computer Science at the Hebrew University of Jerusalem. I have a Bachelor's degree in Statistics and Economics, and a Master's degree in Statistics. I'm probably the only CS student who doesn't know how to code in Python, but I know R, and I love it.

## Research
My research includes developing private methods for non-parametric confidence intervals based on resampling procedures, ratio estimation (odds ratio, relative risk) with associated confidence intervals, and CDF estimation. Adding noise to things is my guilty pleasure. My PhD advisors are Katrina Ligett (CS department) and Yosef Rinott (Statistics department).

<div class="research-tags" aria-label="Research areas">
  <span>Differential privacy</span>
  <span>Statistical inference</span>
  <span>Private data analysis</span>
  <span>Confidence intervals</span>
  <span>CDF estimation</span>
</div>

## Education
<div class="education-grid">
  <div class="education-card">
    <i class="fas fa-graduation-cap" aria-hidden="true"></i>
    <div>
      <strong>Ph.D. Computer Science</strong>
      <span>Hebrew University of Jerusalem</span>
    </div>
  </div>
  <div class="education-card">
    <i class="fas fa-graduation-cap" aria-hidden="true"></i>
    <div>
      <strong>Master's degree in Statistics</strong>
      <span>Statistical inference and data analysis</span>
    </div>
  </div>
  <div class="education-card">
    <i class="fas fa-graduation-cap" aria-hidden="true"></i>
    <div>
      <strong>Bachelor's degree in Statistics and Economics</strong>
      <span>Statistics, probability, and economics</span>
    </div>
  </div>
</div>

## Selected Publications
<div class="selected-publications">
{% assign selected_publications = site.publications | sort: "year" | reverse %}
{% for post in selected_publications limit:3 %}
  <div class="selected-publication">
    {% if post.paperurl %}
      <a href="{{ post.paperurl }}" target="_blank" rel="noopener noreferrer">{{ post.title }}</a>
    {% else %}
      <span>{{ post.title }}</span>
    {% endif %}
    <small>{{ post.year }}{% if post.keywords contains "preprint" %} - Preprint{% elsif post.venue %} - {{ post.venue }}{% endif %}</small>
  </div>
{% endfor %}
</div>

## Other Research Interests
I'm also a Research Assistant of Prof. Gil Kalai at Reichman University, Herzliya, where I work on statistical aspects of experimenting with quantum computers, mainly on the Google supremacy claim made in 2019. We have a line of papers, and you are welcome to check them out on my publications page.
