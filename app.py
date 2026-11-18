"""Interactive Streamlit introduction and resume."""

import json

import streamlit as st

from resume_data import EDUCATION, EXPERIENCE, LANGUAGES, PROFILE, SECTIONS, SKILLS, get_resume

st.set_page_config(
    page_title=f"{PROFILE['name']} | Mainframe & Application Architect",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
      @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');
      :root { --ink: #edf2ff; --muted: #9aa8c2; --accent: #76a9ff; --line: rgba(167,190,230,.16); }
      .stApp { background: radial-gradient(ellipse at 75% -8%, #173369 0, transparent 38%), #09111f; color: var(--ink); }
      html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
      h1, h2, h3 { font-family: 'Manrope', sans-serif !important; color: var(--ink) !important; }
      [data-testid="stSidebar"] { background: #0c1729; border-right: 1px solid var(--line); }
      [data-testid="stSidebar"] .block-container { padding-top: 2rem; }
      .hero { border: 1px solid var(--line); border-radius: 24px; padding: 2.4rem; background: linear-gradient(125deg, rgba(28,53,96,.86), rgba(13,25,44,.94)); box-shadow: 0 20px 70px rgba(0,0,0,.2); }
      .eyebrow { color: #8db9ff; text-transform: uppercase; letter-spacing: .16em; font-size: .75rem; font-weight: 700; }
      .hero h1 { font-size: clamp(2.5rem, 6vw, 4.3rem); margin: .45rem 0 .4rem; letter-spacing: -.055em; }
      .hero .headline { color: #c6d6f3; font-size: 1.15rem; }
      .hero .location { color: var(--muted); margin-top: 1rem; }
      .section-label { color: #91b9ff; text-transform: uppercase; font-size: .72rem; letter-spacing: .16em; font-weight: 700; }
      .card { border: 1px solid var(--line); border-radius: 16px; background: rgba(17,31,53,.74); padding: 1.2rem 1.3rem; height: 100%; }
      .card h3 { margin: .1rem 0 .55rem; font-size: 1.08rem; }
      .muted { color: var(--muted); }
      .tag { display: inline-block; border: 1px solid rgba(118,169,255,.3); color: #bed6ff; background: rgba(58,111,194,.13); border-radius: 100px; padding: .3rem .66rem; margin: .18rem .25rem .18rem 0; font-size: .82rem; }
      .metric { color: #8db9ff; font-family: 'Manrope',sans-serif; font-size: 1.8rem; font-weight: 800; }
      .stButton > button { border-radius: 10px; }
      .stLinkButton > a { border-radius: 10px; }
      div[data-testid="stExpander"] { border: 1px solid var(--line); border-radius: 14px; background: rgba(17,31,53,.5); }
      .stTabs [data-baseweb="tab-list"] { gap: .35rem; }
      .stTabs [data-baseweb="tab"] { background: rgba(17,31,53,.65); border-radius: 9px 9px 0 0; }
      a { color: #9cc4ff !important; }
      @media (max-width: 700px) { .hero { padding: 1.5rem; } }
    </style>
    """,
    unsafe_allow_html=True,
)


def section_heading(eyebrow: str, title: str, intro: str = "") -> None:
    st.markdown(f'<p class="section-label">{eyebrow}</p>', unsafe_allow_html=True)
    st.title(title)
    if intro:
        st.markdown(f'<p class="muted">{intro}</p>', unsafe_allow_html=True)


def render_summary() -> None:
    st.markdown(
        f"""
        <div class="hero">
          <div class="eyebrow">A career at the intersection of legacy and modernisation</div>
          <h1>{PROFILE["name"]}</h1>
          <div class="headline">{PROFILE["headline"]}</div>
          <div class="location">⌖ &nbsp;{PROFILE["location"]}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    st.markdown('<p class="section-label">A little about me</p>', unsafe_allow_html=True)
    st.markdown(PROFILE["summary"])
    col1, col2, col3 = st.columns(3)
    for column, metric, caption in (
        (col1, "17", "people led across four countries"),
        (col2, "10+ years", "building and supporting applications"),
        (col3, "99%", "uptime recorded on a Credit Risk platform"),
    ):
        with column:
            st.markdown(
                f'<div class="card"><div class="metric">{metric}</div><div class="muted">{caption}</div></div>',
                unsafe_allow_html=True,
            )
    st.write("")
    st.markdown('<p class="section-label">Explore the profile</p>', unsafe_allow_html=True)
    st.markdown(
        "Use the navigation to explore my experience, technical toolkit and education. "
        "The **Experience** section can be filtered by company or keywords."
    )
    st.link_button("Connect on LinkedIn ↗", PROFILE["linkedin"])


def render_experience() -> None:
    section_heading(
        "Career",
        "Professional Experience",
        "From core banking systems to cloud-ready platforms, across finance, insurance and technology.",
    )
    companies = [job["company"] for job in EXPERIENCE]
    chosen_companies = st.multiselect("Filter by company", companies, placeholder="All companies")
    search = st.text_input("Search roles and highlights", placeholder="Try: Kafka, architecture, production support…")
    query = search.casefold().strip()
    visible_jobs = [
        job
        for job in EXPERIENCE
        if (not chosen_companies or job["company"] in chosen_companies)
        and (
            not query
            or query in job["company"].casefold()
            or query in job["role"].casefold()
            or any(query in item.casefold() for item in job["highlights"])
        )
    ]
    st.caption(f"Showing {len(visible_jobs)} of {len(EXPERIENCE)} roles")
    for job in visible_jobs:
        with st.expander(f"{job['role']}  ·  {job['company']}  ·  {job['period']}", expanded=not query):
            st.markdown(f"**{job['company']}** &nbsp; · &nbsp; {job['location']}", unsafe_allow_html=True)
            for highlight in job["highlights"]:
                st.markdown(f"- {highlight}")
    if not visible_jobs:
        st.info("No roles match those filters. Try another company or search term.")


def render_skills() -> None:
    section_heading(
        "Toolkit",
        "Core Technical Skills",
        "Search across technologies, delivery methods and business domains.",
    )
    category_names = [group["category"] for group in SKILLS]
    chosen_categories = st.multiselect(
        "Skill groups",
        category_names,
        default=category_names,
        placeholder="Choose skill groups",
    )
    query = st.text_input("Find a skill", placeholder="For example: COBOL, Kafka, GCP…").casefold().strip()
    matches = 0
    columns = st.columns(2)
    for group in SKILLS:
        if group["category"] not in chosen_categories:
            continue
        items = [item for item in group["items"] if not query or query in item.casefold()]
        if not items:
            continue
        matches += len(items)
        column = columns[matches % 2]
        with column:
            tags = "".join(f'<span class="tag">{item}</span>' for item in items)
            st.markdown(
                f'<div class="card"><h3>{group["category"]}</h3>{tags}</div>',
                unsafe_allow_html=True,
            )
            st.write("")
    if not matches:
        st.info("No skills match those filters.")


def render_education() -> None:
    section_heading("Learning", "Education & Professional Development")
    for item in EDUCATION:
        st.markdown(
            f"""
            <div class="card" style="margin-bottom: .8rem">
              <h3>{item["qualification"]}</h3>
              <div>{item["institution"]}</div>
              <div class="muted">{item["period"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.write("")
    st.markdown('<p class="section-label">Languages</p>', unsafe_allow_html=True)
    columns = st.columns(len(LANGUAGES))
    for column, language in zip(columns, LANGUAGES):
        with column:
            st.markdown(
                f'<div class="card"><h3>{language["name"]}</h3><span class="muted">{language["level"]}</span></div>',
                unsafe_allow_html=True,
            )


def render_contact() -> None:
    section_heading(
        "Get in touch",
        "Let’s connect",
        "Interested in mainframe modernisation, application architecture or engineering leadership? Reach out.",
    )
    left, right = st.columns(2)
    with left:
        st.markdown(
            f"""
            <div class="card">
              <h3>{PROFILE["name"]}</h3>
              <div class="muted">{PROFILE["location"]}</div>
              <p><a href="mailto:{PROFILE["email"]}">{PROFILE["email"]}</a></p>
              <p><a href="tel:{PROFILE["phone"].replace(" ", "")}">{PROFILE["phone"]}</a></p>
              <p><a href="{PROFILE["linkedin"]}" target="_blank" rel="noopener noreferrer">LinkedIn profile ↗</a></p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with right:
        st.markdown("#### Profile data")
        st.download_button(
            "Download profile as JSON",
            data=json.dumps(get_resume(), indent=2, ensure_ascii=False),
            file_name="mohit-bhartiya-profile.json",
            mime="application/json",
            use_container_width=True,
        )
with st.sidebar:
    st.markdown("### MB<span style='color:#76a9ff'>.</span>", unsafe_allow_html=True)
    st.caption("PERSONAL PROFILE")
    section_titles = [section["title"] for section in SECTIONS]
    selected_title = st.radio("Navigate", section_titles, label_visibility="collapsed")
    st.divider()
    st.markdown(f"**{PROFILE['name']}**")
    st.caption(PROFILE["headline"])
    st.markdown(f"[LinkedIn profile ↗]({PROFILE['linkedin']})")

if selected_title == "Professional Summary":
    render_summary()
elif selected_title == "Core Technical Skills":
    render_skills()
elif selected_title == "Professional Experience":
    render_experience()
elif selected_title == "Education & Professional Development":
    render_education()
elif selected_title == "Languages":
    section_heading("Communication", "Languages")
    language_columns = st.columns(len(LANGUAGES))
    for column, language in zip(language_columns, LANGUAGES):
        with column:
            st.markdown(
                f'<div class="card"><h3>{language["name"]}</h3><span class="muted">{language["level"]}</span></div>',
                unsafe_allow_html=True,
            )
else:
    render_contact()
