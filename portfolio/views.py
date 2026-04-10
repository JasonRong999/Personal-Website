from django.shortcuts import render


def home(request):
    projects = [
        {
            "name": "Full-Stack Learning Management System",
            "kind": "Personal Project",
            "description": "Designed and built an LMS with React, Next.js, and Django REST Framework, supporting instructor and student roles, course creation, chapters, and rich-text lessons.",
            "image": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=900&q=80",
        },
        {
            "name": "Commercial Product Website",
            "kind": "Yoster Electrical Devices",
            "description": "Developed a product website with React, TypeScript, Node.js, and Django, improving UI/UX and increasing backend request handling capacity by 2-3x.",
            "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=900&q=80",
        },
        {
            "name": "Enterprise Web Applications",
            "kind": "Inspur",
            "description": "Maintained enterprise web applications with React, Java, Spring Boot, RESTful APIs, and SQL while optimizing backend response handling and API latency.",
            "image": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=900&q=80",
        },
    ]
    resume_entries = [
        {
            "date": "Jan 2026 - Present",
            "title": "Software Engineer Intern",
            "place": "Inspur",
            "logo": "portfolio/img/inspur-logo.png",
            "logo_alt": "Inspur logo",
            "details": [
                "Updated and maintained enterprise web applications using HTML, CSS, JavaScript, React, RESTful APIs, Java, Spring Boot, and SQL.",
                "Improved backend performance by restructuring RESTful API endpoints, reducing redundant database queries, and optimizing response handling.",
                "Helped provide cloud computing solutions for 10+ client companies using Inspur Cloud service models including IaaS, PaaS, and SaaS.",
            ],
        },
        {
            "date": "May 2025 - Oct 2025",
            "title": "Full-Stack Developer Intern",
            "place": "Yoster Electrical Devices",
            "details": [
                "Built a commercial product website with React.js, JavaScript, TypeScript, Node.js, and Django.",
                "Increased backend request handling capacity by 2-3x by migrating to Django and restructuring API architecture.",
                "Developed capacitor box panel software with Python and C++, connecting software tools with electrical engineering requirements.",
            ],
        },
        {
            "date": "Aug 2025 - Present",
            "title": "Undeclared / Undecided Major Mentor",
            "place": "UC Irvine",
            "logo": "portfolio/img/uci-logo.png",
            "logo_alt": "UC Irvine Anteaters logo",
            "details": [
                "Organized educational, social, and academic activities that help mentees connect with the UCI community.",
                "Supported mentees through regular contact and helped 3 students find fields of interest and enroll in their target majors.",
            ],
        },
    ]

    context = {
        "name": "Jason Rong",
        "role": "Software Engineer",
        "phone": "9496565800",
        "email": "rongzhiyuan0905@outlook.com",
        "instagram": "rongzhiyuan999",
        "projects": projects,
        "resume_entries": resume_entries,
        "skills": ["Django", "Python", "Java","JavaScript","React","CSS","UI/UX","C++","HTML","ClaudeCode","CodeX","RESTframework","JSX","Node.js","Spring Boot","SQL","MySQL","Frontend craft","Backend development", "Agile methodologies",  "Team collaboration"],
    }
    return render(request, "portfolio/home.html", context)
