import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from main.models import Profile, Skill, Project, Experience, Achievement

def run_population():
    print("Updating portfolio data with exact repository links...")

    # 1. Profile
    Profile.objects.all().delete()
    Profile.objects.create(
        name="Muhammad Musa Qureshi",
        tagline="Computer Scientist | AI/ML & Computer Vision Engineer | Full-Stack & Flutter Developer",
        bio="BS Computer Science graduate from UMT with strong expertise in AI-driven traffic enforcement systems, computer vision algorithms, real-time object detection (YOLOv11), full-stack Django architecture, mobile engineering with Flutter, WordPress development, Prompt Engineering, and Vibe Coding.",
        about_text="I am a passionate Computer Scientist with a comprehensive background in Software Engineering, Deep Learning, Computer Vision, and Rapid Application Prototyping. My flagship engineering work includes 'Smart Eye', an AI-driven traffic enforcement system awarded Top 10 at UMT SST Open House.\n\nI combine classical algorithms with modern AI workflows, leveraging Claude AI, Prompt Engineering, Vibe Coding pipelines, and cross-platform mobile & web development to deliver impactful real-world software solutions.",
        email="mformusa11@gmail.com",
        location="Lahore, Pakistan",
        github="https://github.com/MusaQureshi90",
        linkedin="https://www.linkedin.com/in/musaqureshi90/",
    )
    print("✓ Profile configured")

    # 2. Skills
    Skill.objects.all().delete()
    skills_data = [
        # Programming Languages
        ('Python', 'languages', 95),
        ('C++', 'languages', 90),
        ('Dart', 'languages', 85),
        ('PHP', 'languages', 80),
        ('SQL', 'languages', 85),
        ('HTML5 / CSS3', 'languages', 95),
        ('x86 Assembly', 'languages', 80),

        # Frameworks & Deep Learning
        ('Django', 'frameworks', 92),
        ('Flutter', 'frameworks', 88),
        ('YOLOv11', 'frameworks', 92),
        ('OpenCV', 'frameworks', 90),
        ('EasyOCR', 'frameworks', 85),
        ('Tailwind CSS', 'frameworks', 90),
        ('PyTorch / Hugging Face', 'frameworks', 82),
        ('Streamlit', 'frameworks', 85),

        # Tools & Databases
        ('Git & GitHub', 'tools', 92),
        ('WordPress & CMS', 'tools', 88),
        ('SQLite', 'tools', 90),
        ('MySQL / XAMPP', 'tools', 85),
        ('VS Code', 'tools', 90),
        ('SharedPreferences', 'tools', 85),
        ('EMU8086', 'tools', 80),

        # Core Competencies & Modern AI
        ('Prompt Engineering & LLMs', 'core', 95),
        ('Claude AI & Modern Workflows', 'core', 95),
        ('Vibe Coding & Rapid Prototyping', 'core', 95),
        ('Computer Vision & DIP', 'core', 92),
        ('Natural Language Processing (NLP)', 'core', 85),
        ('Compiler Construction & Parsing', 'core', 85),
        ('Data Structures & Algorithms', 'core', 90),
        ('Object-Oriented Programming (OOP)', 'core', 92),
        ('Game AI (Minimax Algorithm)', 'core', 88),
        ('Operating Systems & Concurrency', 'core', 85),
        ('Embedded Systems & Robotics', 'core', 80),
    ]

    for name, cat, prof in skills_data:
        Skill.objects.create(name=name, category=cat, proficiency=prof)
    print(f"✓ Skills configured ({len(skills_data)} skills added)")

    # 3. All Projects with Exact GitHub Repository URLs
    Project.objects.all().delete()
    projects_data = [
        (
            "Smart Eye: An AI-Driven Traffic Enforcement System (FYP)",
            "An award-winning automated traffic monitoring platform utilizing custom-trained YOLOv11 for real-time helmet violation detection and EasyOCR for automated license plate recognition. Includes a secure Django citizen portal for e-challan verification and digital payment flows.",
            "Python, Django, YOLOv11, OpenCV, EasyOCR, Computer Vision, Deep Learning, SQLite",
            "https://github.com/MusaQureshi90/Smart-Eye-AI-Based-Traffic-Enforcement-System",
            True,
            1
        ),
        (
            "XO ARENA: Next-Gen Cyber Tic-Tac-Toe",
            "An AI-powered cross-platform game featuring the Minimax algorithm with alpha-beta pruning across multiple difficulty tiers, real-time cyber neon aesthetics, audio synthesizers, and achievement unlocks.",
            "Flutter, Dart, Game AI, Minimax Algorithm, Canvas UI",
            "https://github.com/MusaQureshi90/ai-minimax-tictactoe",
            True,
            2
        ),
        (
            "NLP Text Summarizer: Multi-Modal NLP Summarization & Intelligence Suite",
            "An advanced NLP summarization engine processing multi-format texts utilizing tokenization, Hugging Face transformer models (BART), TF-IDF, and frequency scoring heuristics.",
            "Python, NLP, Hugging Face Transformers, BART, PyTorch, NLTK, SpaCy, Scikit-Learn, Streamlit",
            "https://github.com/MusaQureshi90/nlp-smart-text-summarizer",
            False,
            3
        ),
        (
            "Digital Image Processing (DIP) High-Performance Image Filtering & 2D Convolution Framework",
            "A high-performance DIP toolbox executing 2D spatial convolutions, edge detection kernels (Sobel, Prewitt, Laplacian), Gaussian smoothing, and morphological transforms directly on pixel matrices.",
            "Python, Digital Image Processing, Computer Vision, NumPy, OpenCV, Scikit-Image, Convolution Kernels",
            "https://github.com/MusaQureshi90/high-performance-image-filtering-framework",
            False,
            4
        ),
        (
            "Multi-Level Marketing (MLM) Binary Network System",
            "A high-throughput MLM hierarchy engine modeling binary tree topologies, parent-child referral commissions, level-wise reward calculations, and network balance validations.",
            "C++, Algorithms & Data Structures, STL Maps, Tree Topologies, System Design",
            "https://github.com/MusaQureshi90/cpp-mlm-network-system",
            False,
            5
        ),
        (
            "Multithreaded Pi Estimation & High-Performance Concurrency Suite",
            "An Operating Systems systems-level application utilizing POSIX threads and mutex synchronization primitives to compute Pi via Monte Carlo simulations under concurrent thread workloads.",
            "C++, Multithreading, Mutex Synchronization, OS Concurrency, Parallel Computing",
            "https://github.com/MusaQureshi90/cpp-multithreaded-pi-estimation",
            False,
            6
        ),
        (
            "Clinical & Hospital Appointment Management System",
            "A full-stack medical reservation web app built with PHP and MySQL, featuring role-based authorization, doctor scheduling, patient queues, and dynamic prescription storage.",
            "PHP, MySQL, Bootstrap 5, Web Development, Relational Database",
            "https://github.com/MusaQureshi90/php-medical-appointment-system",
            False,
            7
        ),
        (
            "x86 4-Way Traffic Light Controller",
            "A low-level assembly language traffic control emulator running on EMU8086, controlling 4-way intersection timers, state transitions, and hardware interrupts.",
            "x86 Assembly, COAL, Low-Level Programming, Hardware I/O, EMU8086",
            "https://github.com/MusaQureshi90/x86-traffic-lights-controller",
            False,
            8
        ),
        (
            "Banking Management & Transaction System",
            "A core banking engine implementing custom singly linked lists and queue structures to manage user ledger accounts, deposit/withdrawal safety checks, and audit trails.",
            "C++, Data Structures, Singly Linked List",
            "https://github.com/MusaQureshi90/cpp-banking-management-system",
            False,
            9
        ),
        (
            "Autonomous Line-Following Robot",
            "An embedded hardware robotics project combining Arduino microcontroller logic, dual infrared (IR) reflection sensors, and an L298N motor driver for autonomous path tracking.",
            "Arduino, C++, Embedded Systems, L298N, IR Sensors, Robotics",
            "https://github.com/MusaQureshi90/arduino-line-following-robot",
            False,
            10
        ),
        (
            "OOP Car Rental Management System",
            "An enterprise software solution engineered using Object-Oriented Programming (OOP) paradigms with file-based persistence for vehicle inventory, pricing, and client rentals.",
            "C++, Object-Oriented Programming (OOP)",
            "https://github.com/MusaQureshi90/cpp-car-rental-system",
            False,
            11
        ),
        (
            "University Course Management System",
            "An academic portal engine enforcing student course prerequisites, credit hour validations, faculty assignments, and GPA computations using polymorphic OOP design.",
            "C++, Object-Oriented Programming (OOP), Polymorphism",
            "https://github.com/MusaQureshi90/cpp-university-course-management",
            False,
            12
        ),
        (
            "Tic-Tac-Toe (CLI Edition)",
            "A clean command-line implementation of Tic-Tac-Toe with optimized win-state checking algorithms, grid rendering, and turn-based mechanics in C++.",
            "C++, Programming Fundamentals",
            "https://github.com/MusaQureshi90/cpp-cli-tictactoe",
            False,
            13
        ),
        (
            "AI-Driven Tic-Tac-Toe Game Engine (Minimax Search)",
            "An unbeatable desktop AI game engine implementing adversarial Minimax search and depth-limited game tree evaluations paired with a Tkinter interface.",
            "Python, Artificial Intelligence, Minimax Algorithm, Tkinter GUI, Game Theory",
            "https://github.com/MusaQureshi90/ai-minimax-tictactoe",
            False,
            14
        ),
        (
            "MiniLang++ Compiler Front-End & Code Generator",
            "A custom programming language compiler front-end executing lexical tokenization, recursive-descent AST parsing, symbol table resolution, and Three-Address Code (TAC) generation.",
            "Python, Compiler Construction, Lexical Analysis, AST Parsing, Semantic Analysis, Three-Address Code (TAC)",
            "https://github.com/MusaQureshi90/minilang-compiler-pipeline",
            False,
            15
        ),
        (
            "Flutter Task Tracker & To-Do Application",
            "A production-grade offline-first mobile productivity application developed with Flutter and Provider state management, featuring local JSON persistence via SharedPreferences, light/dark theming, and auth flow.",
            "Flutter, Dart, Provider, SharedPreferences, Material 3, Mobile App Development",
            "https://github.com/MusaQureshi90/flutter-task-tracker-app",
            False,
            16
        ),
        (
            "Django Full-Stack Personal Portfolio Website",
            "A modern, highly-responsive personal portfolio platform built with Django and Tailwind CSS featuring dynamic SQLite architecture, real-time message handling, and interactive Canvas rendering.",
            "Python, Django, Tailwind CSS, SQLite, HTML5 / CSS3",
            "https://github.com/MusaQureshi90/personal-portfolio",
            False,
            17
        ),
       
    ]

    for title, desc, stack, link, feat, ord_num in projects_data:
        Project.objects.create(
            title=title,
            description=desc,
            tech_stack=stack,
            github_link=link,
            featured=feat,
            order=ord_num
        )
    print(f"✓ Projects configured ({len(projects_data)} projects with exact repository links added)")

    # 4. Experience & Leadership
    Experience.objects.all().delete()
    experiences_data = [
        (
            "AI & ML Engineering Intern",
            "Big Brains",
            "August 2026",
            "Present",
            "• Collaborating on AI-driven workflows, generative model integration, and rapid application prototyping.\n• Implementing scalable software components and applying prompt engineering techniques to optimize production pipelines.",
            1
        ),
        (
            "Flutter Application Developer Intern",
            "DevelopersHub Corporation",
            "July 2025",
            "August 2025",
            "• Engineered responsive cross-platform mobile interfaces using Flutter & Dart.\n• Implemented Provider state management architecture and local offline storage persistence using SharedPreferences.\n• Built and deployed task workflow systems with dynamic theming and client-side form validations.",
            2
        ),
        (
            "WordPress Developer",
            "Freelance / Client Engagements",
            "April 2024",
            "May 2024",
            "• Architected custom, responsive WordPress websites with SEO optimization, custom plugins, and fast page loads.\n• Managed database integrations, e-commerce payment setups, and responsive UI customization.",
            3
        ),
        (
            "Computer Science & Mathematics Instructor",
            "Al-Haram Academy",
            "February 2019",
            "Present",
            "• Delivered structured curriculum in Computer Science, Logic, and Mathematics for senior students.\n• Mentored students in foundational programming syntax, problem-solving, and analytical thinking.\n• Designed diagnostic assessments and coding exercises for academic performance acceleration.",
            4
        ),
        (
            "Computer Science Teacher & Event Designer",
            "Career School System",
            "May 2025",
            "Feb 2026",
            "• Taught computer applications, digital literacy, and basic algorithmic concepts.\n• Spearheaded official event creative branding, designing marketing collaterals and ceremony announcements.\n• Orchestrated technical setups for institutional ceremonies and academic gatherings.",
            5
        ),
        (
            "Traffic Police Volunteer",
            "City Traffic Police Lahore",
            "2021",
            "2022",
            "• Participated in civic road safety operations and traffic management awareness campaigns across Lahore.\n• Gained real-world domain insights into helmet violation trends that directly informed the Smart Eye FYP architecture.",
            6
        ),
        (
            "Head Boy & Student Council President",
            "APEX Group of Colleges (Tajbagh Campus)",
            "2021",
            "2022",
            "• Led the central student body council, managing inter-college competitions and student grievance channels.\n• Represented the student body during administrative forums and official academic events.",
            7
        ),
    ]

    for role, org, start, end, desc, ord_num in experiences_data:
        Experience.objects.create(
            role=role,
            organization=org,
            start_date=start,
            end_date=end,
            description=desc,
            order=ord_num
        )
    print(f"✓ Experience & Leadership configured ({len(experiences_data)} roles added)")

    # 5. Achievements, Honors & Social Service
    Achievement.objects.all().delete()
    achievements_data = [
        (
            "Top 10 Finalist & Certificate of Excellence",
            "University of Management and Technology (UMT SST Exhibition)",
            "July 2026",
            "Ranked among the Top 10 projects out of 160+ competing teams at the UMT SST Final Year Projects Exhibition for the engineering design of 'Smart Eye: An AI-Driven Traffic Enforcement System'.",
            1
        ),
        (
            "Claude Artificial Intelligence",
            "National Vocational and Technical Training Commission (NAVTTC)",
            "2026",
            "Professional training in Claude AI architectures, LLM workflows, contextual reasoning, and real-world AI applications under the NAVTTC program.",
            2
        ),
        (
            "Youth Mentorship & Education Outreach Drive",
            "Community Welfare & School Outreach",
            "2025",
            "Organized an outreach visit to an underprivileged and orphan children's school; delivered interactive lectures on the importance of education, hard work, and foundational tech skills, accompanied by youth mentorship and developmental activities.",
            3
        ),
        (
            "Orphanage Healthcare & Hygiene Kit Distribution",
            "Community Welfare & Social Service",
            "2025",
            "Led a humanitarian distribution drive at an orphanage, supplying essential health and personal hygiene kits to underprivileged children along with wellness awareness sessions.",
            4
        ),
        (
            "Head Boy Certificate of Distinction & Leadership Shield",
            "APEX Group of Colleges",
            "2022",
            "Awarded in recognition of student leadership, institutional service, and academic discipline while presiding over the student council.",
            5
        ),
        (
            "Civic Service Commendation",
            "City Traffic Police Lahore",
            "2026",
            "Commended for volunteer public safety contributions and participation in civic traffic regulation drives.",
            6
        ),
    ]

    for title, issuer, date, desc, ord_num in achievements_data:
        Achievement.objects.create(
            title=title,
            issuer=issuer,
            date=date,
            description=desc,
            order=ord_num
        )
    print(f"✓ Achievements configured ({len(achievements_data)} records added)")

    print("\n🎉 ALL EXACT REPOSITORIES MAPPED AND DATABASE UPDATED SUCCESSFULLY!")

if __name__ == '__main__':
    run_population()