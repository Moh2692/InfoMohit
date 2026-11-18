"""Structured profile data transcribed from Mohit Bhartiya's resume."""

PROFILE = {
    "name": "Mohit Bhartiya",
    "headline": "Mainframe Technical Lead | Mainframe & Application Architect",
    "location": "Warsaw, Poland",
    "phone": "+48 579 170 730",
    "email": "mohit.bhartiya.1993@gmail.com",
    "linkedin": "https://www.linkedin.com/in/mohit-bhartiya/",
    "summary": (
        "Technology professional experienced in designing, developing, supporting and "
        "modernising business-critical applications in Banking and Financial Services. "
        "Deep expertise in IBM mainframe technologies, including COBOL, PL/I, JCL, CICS, "
        "DB2 and IMS DB, complemented by Java, Spring Boot, REST APIs, IBM MQ and Apache "
        "Kafka. Experienced in technical leadership, application architecture, "
        "cross-functional delivery and production support across Securities, Custody, "
        "Corporate Actions, SWIFT/financial messaging and Credit Risk. Led distributed "
        "engineering teams of up to 17 people and contributed to mainframe modernisation, "
        "event-driven architecture, PaaS adoption and CI/CD implementation. Combines "
        "strong legacy-platform knowledge with modern engineering practices and a focus "
        "on reliable, scalable solutions."
    ),
}

SECTIONS = [
    {"key": "summary", "title": "Professional Summary"},
    {"key": "skills", "title": "Core Technical Skills"},
    {"key": "experience", "title": "Professional Experience"},
    {"key": "education", "title": "Education & Professional Development"},
    {"key": "languages", "title": "Languages"},
    {"key": "contact", "title": "Contact"},
]

SKILLS = [
    {
        "category": "Mainframe & legacy systems",
        "items": [
            "COBOL", "PL/I", "JCL", "CICS", "VSAM", "IMS DB", "DL/I", "IBM DB2",
            "Batch processing", "Mainframe application support",
        ],
    },
    {
        "category": "Architecture & modernisation",
        "items": [
            "Application architecture", "Technical design", "Legacy modernisation",
            "Mainframe migration", "Modularisation", "REST APIs", "Microservices",
            "Event-driven architecture",
        ],
    },
    {
        "category": "Programming & frameworks",
        "items": ["Java 17", "Spring", "Spring Boot", "SQL", "Python"],
    },
    {
        "category": "Messaging & financial protocols",
        "items": ["IBM MQ", "Apache Kafka", "SWIFT MT", "SWIFT MX", "Financial messaging"],
    },
    {
        "category": "Databases & data",
        "items": [
            "IBM DB2", "IMS DB", "Oracle", "MySQL", "PostgreSQL",
            "Database design", "Performance optimisation",
        ],
    },
    {
        "category": "DevOps, cloud & platforms",
        "items": [
            "Jenkins", "Git", "Bitbucket", "Docker", "Kubernetes", "OpenShift", "GCP",
            "Ansible", "Terraform", "Argo CD", "Maven", "Sonar",
        ],
    },
    {
        "category": "Scheduling, operations & monitoring",
        "items": [
            "Control-M", "OPC", "Production support", "Incident management",
            "Root-cause analysis", "ELK Stack", "Kibana", "Grafana",
        ],
    },
    {
        "category": "Tools & delivery",
        "items": [
            "Jira", "Confluence", "ServiceNow", "Changeman", "Endevor", "File-AID",
            "IBM Developer for z/OS (IDz)", "Topaz", "Agile", "Scrum", "Kanban",
            "Waterfall",
        ],
    },
    {
        "category": "Business domains",
        "items": [
            "Securities", "Custody", "Corporate Actions", "NOSTRO", "SWIFT",
            "OTC trades", "Asset Servicing", "Credit Risk", "Insurance", "Pensions",
        ],
    },
]

EXPERIENCE = [
    {
        "company": "UniCredit",
        "role": "Product Specialist (Software Development Engineering)",
        "location": "Warsaw, Poland",
        "period": "Sep 2024 – Present",
        "highlights": [
            "Lead a cross-functional team of 17 developers and business analysts across Poland, Austria, Germany and India, supporting delivery across Java and mainframe technologies.",
            "Act as application lead and subject-matter expert for business-critical Securities applications, with a focus on SWIFT, NOSTRO, Custody and Corporate Actions.",
            "Drive delivery across the product lifecycle, aligning technical execution with business objectives and coordinating requirements with business stakeholders.",
            "Lead the design and development of applications and REST APIs using COBOL, PL/I and Java.",
            "Coordinate production support and incident management, including on-call response to critical production issues.",
            "Lead an in-flight initiative to modernise and migrate COBOL-based mainframe applications towards Google Cloud Platform (GCP).",
            "Enhance source-code repository practices in Bitbucket, including a pilot involving code-assistant capabilities.",
        ],
    },
    {
        "company": "BEC",
        "role": "Architect (Software Engineer)",
        "location": "Warsaw, Poland",
        "period": "Dec 2022 – Aug 2024",
        "highlights": [
            "Served as a senior technical resource in an Agile team developing, enhancing and modernising a Credit Risk calculation platform built on COBOL, DB2, CICS and Java 17/Spring Boot.",
            "Acted as Scrum Master and deputy technical lead for a 10-member team, facilitating delivery, backlog prioritisation and coordination across technical and business teams.",
            "Led technical design and architecture across mainframe and open-architecture systems, with emphasis on scalability, reliability and maintainability.",
            "Redesigned complex COBOL modules and optimised DB2 tables to improve application performance.",
            "Contributed to solution architecture, Kafka event design, component separation, database schemas and API contracts, enabling parallel delivery by multiple development sub-teams.",
            "Coordinated go-live preparation, feature delivery, sprint planning and stakeholder collaboration.",
            "Provided third-line production support and on-call assistance; the CV records 99% system uptime and resolution of 90% of incidents within SLA.",
            "Created and maintained CI/CD pipelines and supported vulnerability remediation in PaaS components.",
            "Mentored junior engineers and documented technical solutions and team knowledge in Confluence.",
            "Achievement: Led development and migration from COBOL/MQ-based mainframe components to OpenShift PaaS components, implementing event-driven architecture and CI/CD using Git, Jenkins, Docker, Sonar and Kubernetes.",
        ],
    },
    {
        "company": "Credit Suisse AG",
        "role": "Application Software Developer (AVP)",
        "location": "Wroclaw, Poland",
        "period": "Feb 2020 – Nov 2022",
        "highlights": [
            "Developed and supported business-critical applications across Custody, Financial Messaging, Asset Servicing, SWIFT, OTC trades, regulatory trade checks, Corporate Actions and BI reporting.",
            "Built and enhanced applications using PL/I and Java, contributing to a reported 20% improvement in system efficiency.",
            "Designed and delivered automated data pipelines and dashboards using Alteryx and Tableau, reducing manual effort by 70%.",
            "Managed and scheduled critical batch workloads using Control-M and provided third-line/on-call support, resolving 90% of incidents within SLA.",
            "Collaborated with business, technology and ITIL stakeholders to deliver enhancements aligned with SWIFT annual releases and regulatory requirements.",
            "Contributed to modernising monolithic PL/I applications into Java REST API-based services using Spring and Apache Kafka.",
            "Designed and implemented a Kogito-based rule engine, reducing per-request processing time by 70% and operational costs by 40%.",
            "Automated extraction and delivery of Tableau and Alteryx reporting, saving approximately four person-days per month.",
            "Received an accelerated promotion in recognition of delivery and contributions.",
        ],
    },
    {
        "company": "Allianz Technologies",
        "role": "Senior Software Engineer",
        "location": "Pune, India",
        "period": "Nov 2019 – Jan 2020",
        "highlights": [
            "Contributed to end-to-end development of a new insurance product, creating PL/I and DB2 modules and supporting process optimisation.",
            "Participated in Scrum ceremonies, estimated story complexity and supported delivery planning and quality reviews.",
        ],
    },
    {
        "company": "Capita",
        "role": "Software Consultant",
        "location": "Pune, India",
        "period": "Jun 2019 – Nov 2019",
        "highlights": [
            "Enhanced existing PL/I and COBOL applications supporting insurance and pension products.",
            "Developed complex IMS data scans to support business analysis and insights.",
            "Supported batch testing and data-integrity activities during key delivery stages.",
            "Automated a repetitive manual process using VB scripts, reducing manual intervention.",
            "Prepared an Automated Code Review (ACR) framework to improve the code-review process.",
        ],
    },
    {
        "company": "Cognizant Technology Solutions",
        "role": "Associate",
        "location": "Kolkata, India",
        "period": "Feb 2016 – Jun 2019",
        "highlights": [
            "Worked as a contractor supporting Credit Suisse applications across Custody, SWIFT/Financial Messaging and Asset Servicing.",
            "Designed and implemented enhancements to core PL/I applications and supported major and minor releases using Agile and Waterfall delivery approaches.",
            "Contributed to migration from IMS to DB2 and modernisation initiatives, including CORBA-to-web-services migration and replacement of VB scripts with application-based solutions.",
            "Optimised Control-M job scheduling and DB2 interactions for critical application modules.",
            "Led requirements discussions, supported scope definition and proposed solutions aligned with business objectives.",
            "Resolved production issues, handled incident escalations and prepared root-cause analysis reports.",
            "Achievement: Defined and implemented central modules for IMS decoupling, streamlining processing and reducing dependencies.",
        ],
    },
]

EDUCATION = [
    {
        "qualification": "Postgraduate Program in DevOps",
        "institution": "Purdue University (Edureka)",
        "period": "Jun 2024 – Aug 2025",
    },
    {
        "qualification": "B.E., Electronics & Telecommunication",
        "institution": "Maharashtra Institute of Technology Academy of Engineering, Pune, India",
        "period": "Jun 2011 – Jun 2015",
    },
]

LANGUAGES = [
    {"name": "Hindi", "level": "Native"},
    {"name": "English", "level": "C2"},
    {"name": "German", "level": "B1; speaking and interaction A2"},
]


def get_section(section_key: str) -> dict[str, object] | None:
    """Return one resume section in the API's public response shape."""
    section_content: dict[str, object] = {
        "summary": PROFILE["summary"],
        "skills": SKILLS,
        "experience": EXPERIENCE,
        "education": EDUCATION,
        "languages": LANGUAGES,
        "contact": {
            "location": PROFILE["location"],
            "phone": PROFILE["phone"],
            "email": PROFILE["email"],
            "linkedin": PROFILE["linkedin"],
        },
    }
    section = next((item for item in SECTIONS if item["key"] == section_key), None)
    if section is None:
        return None
    return {**section, "content": section_content[section_key]}


def get_resume() -> dict[str, object]:
    """Return all profile content in a JSON-serializable structure."""
    return {
        **PROFILE,
        "sections": SECTIONS,
        "skills": SKILLS,
        "experience": EXPERIENCE,
        "education": EDUCATION,
        "languages": LANGUAGES,
    }
