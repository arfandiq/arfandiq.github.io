/* Edit data/*.json for content. Photo lists are discovered by scripts/build.py. */
'use strict';
const $ = selector => document.querySelector(selector);
const esc = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const safePhoto = src => typeof src === 'string' && src.startsWith('assets/photos/') && !src.includes('..');
const C = window.CONTENT;
const P = C.profile;
const allEntries = [...C.projects, ...C.work, ...C.internship, ...C.organization, ...C.awards];
const validPhotos = entry => (entry.photos || []).filter(photo => safePhoto(photo.src));
const detailText = entry => [...entry.paragraphs, ...entry.bullets].join(' ');
const detailsHTML = entry => entry.paragraphs.map(p => `<p>${esc(p)}</p>`).join('') + (entry.bullets.length ? `<ul class="detail-bullets">${entry.bullets.map(b => `<li>${esc(b)}</li>`).join('')}</ul>` : '');

function thumbnail(entry) {
  const photo = validPhotos(entry)[0];
  return photo ? `<img class="entry-thumb" src="${esc(photo.src)}" alt="${esc(photo.alt)}" loading="lazy">` : '';
}
function removeBrokenImages(scope = document) {
  scope.querySelectorAll('img').forEach(img => {
    img.addEventListener('error', () => {
      const featured = img.closest('.project-photo');
      if (featured) {
        const card = featured.closest('.project-card');
        featured.remove(); card.classList.remove('has-photo'); card.classList.add('text-only');
      } else {
        const figure = img.closest('figure');
        if (figure && figure.parentElement?.classList.contains('gallery')) {
          const gallery = figure.parentElement; figure.remove();
          if (!gallery.children.length) gallery.remove();
        } else img.remove();
      }
    }, { once: true });
  });
}
function galleryHTML(photos) {
  const valid = photos.filter(photo => safePhoto(photo.src));
  if (!valid.length) return '';
  return `<div class="gallery">${valid.map(photo => `<figure><a href="${esc(photo.src)}" target="_blank" rel="noopener" aria-label="Open full photo: ${esc(photo.alt)}"><img src="${esc(photo.src)}" alt="${esc(photo.alt)}" loading="lazy"></a>${photo.caption ? `<figcaption>${esc(photo.caption)}</figcaption>` : ''}</figure>`).join('')}</div>`;
}

// Identity, complete professional summary, education, and skills.
document.title = P.brand;
document.querySelectorAll('.brand').forEach(el => el.textContent = P.brand);
$('#introduction').textContent = P.introduction;
$('#hero-title').innerHTML = P.heroTitle.map((line,i) => i === P.heroTitle.length - 1 ? `<em>${esc(line)}</em>` : esc(line)).join('<br>');
$('#professional-summary').textContent = P.summary;
const edu = P.education;
$('#education').innerHTML = `<span class="eyebrow">EDUCATION / ${esc(edu.date)}</span><h3>${esc(edu.org)}</h3><p>${esc(edu.title)}</p><p>${esc(edu.location)}</p><span class="status">${esc(edu.credential)} · ${esc(edu.status)}</span><p class="small">${esc(edu.description)}</p>${galleryHTML(C.educationPhotos)}`;
const technical = ['Robot Operating System 1 (ROS 1)','Robot Operating System 2 (ROS 2)','Python','C++','C'];
$('#technical-skills').innerHTML = P.skills.filter(s => technical.includes(s)).map(s => `<span>${esc(s)}</span>`).join('');
$('#people-skills').innerHTML = P.skills.filter(s => !technical.includes(s)).map(s => `<span>${esc(s)}</span>`).join('');
$('#tools').innerHTML = P.tools.map(tool => `<span>${esc(tool)}</span>`).join('');
$('#personal-quote').innerHTML = `${esc(P.quote.text)}<span class="quote-end" aria-hidden="true">”</span>`;
$('#quote-author').textContent = P.quote.author;
document.querySelectorAll('a[href^="mailto:"]').forEach(a => { a.href = 'mailto:' + P.email; if (a.classList.contains('email')) a.textContent = P.email + ' ↗'; });
document.querySelector('a[href*="linkedin.com"]').href = P.linkedin;
document.querySelector('a[href*="github.com"]').href = P.github;

// Social links are editable in data/profile.json; NGL has a distinct message action.
$('#social-links').innerHTML = (P.socials || []).map((social,i) => `<a class="social-card" href="${esc(social.url)}" target="_blank" rel="noopener noreferrer"><span class="social-number">0${i+1}</span><h3>${esc(social.name)}</h3><span class="social-handle">${esc(social.handle)}</span><span class="social-arrow" aria-hidden="true">↗</span></a>`).join('');
if (P.anonymousMessage) {
  $('#anonymous-link').href = P.anonymousMessage.url;
  $('#anonymous-link').innerHTML = `${esc(P.anonymousMessage.label)} <span aria-hidden="true">↗</span>`;
} else $('.anonymous-message').hidden = true;

// Original portrait and original design are independent optional uploads.
const portrait = C.profilePhotos.find(photo => safePhoto(photo.src));
if (portrait) {
  const figure = $('#hero-original'); const img = new Image();
  img.alt = portrait.alt; img.decoding = 'async';
  img.onload = () => { figure.hidden = false; $('.hero').classList.add('has-original'); };
  img.onerror = () => { figure.hidden = true; $('.hero').classList.remove('has-original'); };
  img.src = portrait.src; figure.append(img);
}
if (C.designPhotos.some(photo => safePhoto(photo.src))) {
  const design = $('#original-design');
  design.innerHTML = galleryHTML(C.designPhotos); design.hidden = false;
  design.querySelectorAll('img').forEach(img => {
    img.addEventListener('error', () => { img.closest('figure').remove(); if (!design.querySelector('figure')) design.hidden = true; }, {once:true});
  });
}

// Exactly three featured entries, controlled through data/projects.json.
const featured = C.projects.filter(p => p.featured).sort((a,b) => a.featuredOrder - b.featuredOrder);
$('#featured').innerHTML = featured.map((p,i) => {
  const photo = validPhotos(p)[0];
  return `<article class="project-card reveal ${photo ? 'has-photo' : 'text-only'}">${photo ? `<button class="project-photo" data-detail="${esc(p.id)}" aria-label="View ${esc(p.title)}"><img src="${esc(photo.src)}" alt="${esc(photo.alt)}" loading="lazy"></button>` : ''}<div class="project-info"><div class="project-meta"><span>0${i+1} / ${esc(p.category.toUpperCase())}</span><span>${esc(p.date)}</span></div><h3 class="long-title">${esc(p.title)}</h3><p>${esc(p.summary)}</p><div class="tags">${(p.tags || []).map(t => `<span>${esc(t)}</span>`).join('')}</div><button class="text-link" data-detail="${esc(p.id)}">Explore project <span aria-hidden="true">↗</span></button></div></article>`;
}).join('');
$('#project-count').textContent = C.projects.length;
$('#category').innerHTML = '<option value="">All disciplines</option>' + [...new Set(C.projects.map(p => p.category))].map(c => `<option>${esc(c)}</option>`).join('');
function renderArchive() {
  const term = $('#search').value.toLowerCase(); const category = $('#category').value;
  const filtered = C.projects.filter(p => (!category || p.category === category) && `${p.title} ${p.summary} ${detailText(p)}`.toLowerCase().includes(term));
  $('#project-list').innerHTML = filtered.map(p => `<button class="archive-row" data-detail="${esc(p.id)}"><small>${esc(p.date)}</small><b>${thumbnail(p)}${esc(p.title)}</b><span aria-hidden="true">↗</span></button>`).join('');
  $('#result-count').textContent = filtered.length ? `${filtered.length} ${filtered.length === 1 ? 'project' : 'projects'}` : 'No projects found. Try another keyword.';
  removeBrokenImages($('#project-list'));
}
$('#archive-toggle').onclick = () => {
  const open = $('#archive').hidden; $('#archive').hidden = !open;
  $('#archive-toggle').setAttribute('aria-expanded',open);
  $('#archive-toggle').textContent = open ? 'Close archive −' : 'Explore all projects +';
  if (open) renderArchive();
};
$('#search').oninput = renderArchive; $('#category').onchange = renderArchive;

function experience(group) {
  $('#experience-list').setAttribute('aria-labelledby',`tab-${group}`);
  $('#experience-list').innerHTML = C[group].map(p => `<button class="experience-row" data-detail="${esc(p.id)}"><span>${esc(p.date)}</span><div>${thumbnail(p)}<h3>${esc(p.title)}</h3><p>${esc(p.org)}</p></div><span aria-hidden="true">↗</span></button>`).join('');
  removeBrokenImages($('#experience-list'));
}
const tabs = [...document.querySelectorAll('[data-tab]')];
tabs.forEach((button,i) => {
  button.querySelector('sup').textContent = String(C[button.dataset.tab].length).padStart(2,'0');
  button.onclick = () => {
    tabs.forEach(t => { t.setAttribute('aria-selected',t === button); t.tabIndex = t === button ? 0 : -1; });
    experience(button.dataset.tab);
  };
  button.onkeydown = e => {
    const target = {ArrowRight:(i+1)%tabs.length,ArrowLeft:(i+tabs.length-1)%tabs.length,Home:0,End:tabs.length-1}[e.key];
    if (target !== undefined) { e.preventDefault(); tabs[target].focus(); tabs[target].click(); }
  };
});
experience('work');

$('#awards').innerHTML = C.awards.map((p,i) => `<button class="award-row reveal" data-detail="${esc(p.id)}"><span class="medal" aria-hidden="true">${i === 0 ? '✦' : '◇'}</span><div>${thumbnail(p)}<h3>${esc(p.title)}</h3><p>${esc(p.org)}</p></div><small>${esc(p.date)}</small><span aria-hidden="true">↗</span></button>`).join('');
$('#articles').className = 'article-grid';
$('#articles').innerHTML = C.articles.map(a => {
  const photo = validPhotos(a)[0];
  return `<a class="article-card" href="${esc(a.url)}" target="_blank" rel="noopener noreferrer">${photo ? `<img src="${esc(photo.src)}" alt="${esc(photo.alt)}" loading="lazy">` : ''}<div class="article-meta"><span>${esc(a.publisher)}</span>${a.date ? `<span>${esc(a.date)}</span>` : ''}</div><p class="article-kind">${esc(a.kind || 'Feature')}</p><h3>${esc(a.title)}</h3><p>${esc(a.description)}</p><span class="article-read">Read original article <span aria-hidden="true">↗</span></span></a>`;
}).join('');

// The complete CV text, including every bullet, lives in the detail dialog.
let returnFocus;
function openDetail(id) {
  const entry = allEntries.find(p => p.id === id); if (!entry) return;
  returnFocus = document.activeElement;
  $('#detail-body').innerHTML = `<p class="eyebrow">${esc(entry.category || 'EXPERIENCE')} / ${esc(entry.date)}</p><h2 id="detail-title">${esc(entry.title)}</h2>${entry.org ? `<p class="detail-organization">${esc(entry.org)}</p>` : ''}${entry.location ? `<p class="detail-location">${esc(entry.location)}</p>` : ''}${detailsHTML(entry)}${galleryHTML(validPhotos(entry))}`;
  removeBrokenImages($('#detail-body'));
  $('#detail').showModal(); $('#detail').scrollTop = 0;
  document.body.classList.add('modal-open');
}
document.addEventListener('click', e => {
  const button = e.target.closest('[data-detail]'); if (button) openDetail(button.dataset.detail);
});
$('.close').onclick = () => $('#detail').close();
$('#detail').addEventListener('click', e => {
  if (e.target === $('#detail')) {
    const rect = e.target.getBoundingClientRect();
    if (e.clientX < rect.left || e.clientX > rect.right || e.clientY < rect.top || e.clientY > rect.bottom) e.target.close();
  }
});
$('#detail').addEventListener('close', () => { document.body.classList.remove('modal-open'); returnFocus?.focus(); });
$('.menu').onclick = () => { const open = $('nav').classList.toggle('open'); $('.menu').setAttribute('aria-expanded',open); };
document.querySelectorAll('nav a').forEach(a => a.onclick = () => { $('nav').classList.remove('open'); $('.menu').setAttribute('aria-expanded',false); });
document.addEventListener('keydown', e => { if (e.key === 'Escape' && $('nav').classList.contains('open')) { $('nav').classList.remove('open'); $('.menu').setAttribute('aria-expanded',false); $('.menu').focus(); } });
removeBrokenImages();

if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const observer = new IntersectionObserver(entries => entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('visible'); observer.unobserve(e.target); }
  }), {threshold:.08});
  document.querySelectorAll('.reveal').forEach((el,i) => { el.classList.add('ready'); el.style.transitionDelay = `${i%2*65}ms`; observer.observe(el); });
}
let ticking = false;
addEventListener('scroll', () => {
  if (!ticking) {
    requestAnimationFrame(() => { const max = document.documentElement.scrollHeight-innerHeight; $('.progress').style.width = `${max > 0 ? scrollY/max*100 : 0}%`; ticking = false; });
    ticking = true;
  }
}, {passive:true});
