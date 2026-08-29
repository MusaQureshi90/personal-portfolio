import os
import sys
from pathlib import Path
import django

# Base directory ko Python path me add karein
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from main.models import Profile, Skill, Project, Experience, Achievement

# ... Baqi sara run() function code wahi rahega jo pehle diya tha

def run():
    # 1. Profile
    Profile.objects.all().delete()
    profile = Profile.objects.create(
        name="Muhammad Musa Qureshi",
        tagline="Computer Scientist | AI, Deep Learning & Software Engineer",
        bio="BS Computer Science graduate from UMT Lahore. Passionate about building robust Computer Vision architectures, intelligent systems with Deep Learning, interactive game logic, and full-stack software solutions.",
        about_text="I am a dedicated Computer Scientist with a strong foundation in Artificial Intelligence, Deep Learning, Image Processing, and Full-Stack Engineering. Proven record of developing intelligent systems like 'Smart Eye' (AI Traffic Enforcement with YOLOv8 & OCR) and high-performance algorithms. Beyond engineering, I possess over 5 years of teaching and technical mentorship experience, leading practical IT workshops, and community volunteering.",
        email="mformusa11@gmail.com",
        github="https://github.com/MusaQureshi90",
        linkedin="https://www.linkedin.com/in/musaqureshi90/",
        location="Lahore, Pakistan"
    )
    print("✅ Profile Created")

    # 2. Skills
    Skill.objects.all().delete()
    skills_data = [
        # Languages
        ('Python', 'languages', 95),
        ('C++', 'languages', 90),
        ('JavaScript', 'languages', 80),
        ('PHP', 'languages', 75),
        ('SQL', 'languages', 85),
        ('HTML5 / CSS3', 'languages', 95),
        # Frameworks & AI
        ('Django', 'frameworks', 90),
        ('OpenCV', 'frameworks', 92),
        ('YOLO (v8)', 'frameworks', 90),
        ('EasyOCR', 'frameworks', 85),
        ('Tailwind CSS', 'frameworks', 88),
        ('Unity / C#', 'frameworks', 75),
        ('Flutter', 'frameworks', 70),
        # Tools & Databases
        ('SQLite', 'tools', 90),
        ('MySQL / XAMPP', 'tools', 85),
        ('Git & GitHub', 'tools', 90),
        ('Linux / VS Code', 'tools', 88),
        # Core
        ('Computer Vision & DIP', 'core', 92),
        ('Data Structures & Algorithms', 'core', 90),
        ('Object-Oriented Programming', 'core', 95),
        ('Game AI (Minimax Algorithm)', 'core', 88),
        ('Operating Systems & Concurrency', 'core', 82),
    ]
    for name, cat, prof in skills_data:
        Skill.objects.create(name=name, category=cat, proficiency=prof)
    print("✅ Skills Created")

    # 3. Projects
    Project.objects.all().delete()
    projects_data = [
        {
            'title': 'Smart Eye: An AI-Driven Traffic Enforcement System',
            'description': 'Dual-class YOLOv8 model for automated helmet detection, OpenCV + EasyOCR pipeline for license plate recognition, and a full-stack Django citizen portal for automated e-challan generation and verification.',
            'tech_stack': 'Python, YOLOv8, OpenCV, EasyOCR, Django, SQLite',
            'github_link': 'https://github.com/MusaQureshi90',
            'live_link': None,
            'featured': True,
            'order': 1
        },
        {
            'title': 'XO ARENA: Next-Gen Cyber Tic-Tac-Toe',
            'description': 'Advanced 2D neon strategy game featuring an unbeatable Minimax AI algorithm with adaptive depth, pass-and-play multiplayer, daily challenges, and custom progression themes.',
            'tech_stack': 'Python / Game Engine, Minimax AI, Cyberpunk UI, Game Math',
            'github_link': 'https://github.com/MusaQureshi90',
            'live_link': None,
            'featured': True,
            'order': 2
        },
        {
            'title': 'NLP Text Summarizer',
            'description': 'Natural Language Processing pipeline designed to summarize lengthy text documents into precise executive bullet points using text processing models.',
            'tech_stack': 'Python, NLTK, NLP Algorithms',
            'github_link': 'https://github.com/MusaQureshi90',
            'live_link': None,
            'featured': False,
            'order': 3
        },
        {
            'title': 'Digital Image Processing (DIP) Filtering Suite',
            'description': 'Custom spatial and frequency domain image filters developed from scratch, including Gaussian blur, edge detection masks (Sobel, Laplacian), and noise reduction.',
            'tech_stack': 'Python, OpenCV, NumPy, DIP Math',
            'github_link': 'https://github.com/MusaQureshi90',
            'live_link': None,
            'featured': False,
            'order': 4
        },
        {
            'title': 'Multi-Level Marketing (MLM) System',
            'description': 'Complex algorithmic tree system with user registration, automated referral bonus calculation (Rs. 100 per referral), financial withdrawal tracking, and admin dashboard.',
            'tech_stack': 'C++, Algorithms & Data Structures',
            'github_link': 'https://github.com/MusaQureshi90',
            'live_link': None,
            'featured': False,
            'order': 5
        },
        {
            'title': 'Multithreaded Pi Estimation',
            'description': 'Operating Systems implementation estimating Pi value using Maclaurin series for arc tan(x) optimized with POSIX multithreading and concurrency control.',
            'tech_stack': 'C++, POSIX Threads, OS Concurrency',
            'github_link': 'https://github.com/MusaQureshi90',
            'live_link': None,
            'featured': False,
            'order': 6
        },
        {
            'title': 'Medical Appointment & Management System',
            'description': 'Full-stack database management system for clinics handling patient scheduling, doctor appointments, medical records, and billing.',
            'tech_stack': 'PHP, MySQL, XAMPP, HTML/CSS',
            'github_link': 'https://github.com/MusaQureshi90',
            'live_link': None,
            'featured': False,
            'order': 7
        },
        {
            'title': 'Banking System (Data Structures)',
            'description': 'Console-based banking management application utilizing custom linked lists, queues, and file handling for transactional security.',
            'tech_stack': 'C++, Data Structures, File I/O',
            'github_link': 'https://github.com/MusaQureshi90',
            'live_link': None,
            'featured': False,
            'order': 8
        },
        {
            'title': 'Autonomous Arduino Line-Following Vehicle',
            'description': 'Embedded systems hardware vehicle with infrared IR sensor array and logic controllers for autonomous precision track navigation.',
            'tech_stack': 'Arduino, C++, IR Sensors, Digital Logic',
            'github_link': 'https://github.com/MusaQureshi90',
            'live_link': None,
            'featured': False,
            'order': 9
        },
        {
            'title': 'OOP Car Rental & Student Management Systems',
            'description': 'Modular Object-Oriented software architectures implementing inheritance, polymorphism, encapsulation, and persistent record storage.',
            'tech_stack': 'C++, OOP Principles',
            'github_link': 'https://github.com/MusaQureshi90',
            'live_link': None,
            'featured': False,
            'order': 10
        },
        {
            'title': 'Function-Based BINGO & Console Games',
            'description': 'Modular structured C++ games implementing matrix manipulation, randomized board generation, and interactive turn-based console logic.',
            'tech_stack': 'C++, Programming Fundamentals',
            'github_link': 'https://github.com/MusaQureshi90',
            'live_link': None,
            'featured': False,
            'order': 11
        }
    ]
    for p in projects_data:
        Project.objects.create(**p)
    print("✅ Projects Created")

    # 4. Experience
    Experience.objects.all().delete()
    exp_data = [
        {
            'role': 'Computer Science & Mathematics Instructor',
            'organization': 'Al-Haram Academy',
            'start_date': '2019',
            'end_date': 'Present',
            'description': 'Delivering comprehensive curriculum instruction for Matric & Intermediate students in Advanced Mathematics and Computer Science.\nConducted 2-Month Intensive Practical IT Workshops covering OS installations (Windows/Linux), BIOS configuration, system troubleshooting, hardware diagnostics, error handling, and productivity suites.',
            'order': 1
        },
        {
            'role': 'Computer Science Teacher & Event Designer',
            'organization': 'Career School System',
            'start_date': 'May 2025',
            'end_date': 'Feb 2026',
            'description': 'Taught Computer Science coursework and served as primary digital media and event designer for institutional ceremonies, annual events, and student campaigns.',
            'order': 2
        },
        {
            'role': 'Student Traffic Police Volunteer',
            'organization': 'City Traffic Police Lahore',
            'start_date': '2024',
            'end_date': '2026',
            'description': 'Active civic volunteer engaged in road safety enforcement awareness, helmet compliance campaigns, and public traffic regulation drives across Lahore.',
            'order': 3
        },
        {
            'role': 'Head Boy & Student Council President',
            'organization': 'APEX Group of Colleges (Tajbagh Campus)',
            'start_date': '2020',
            'end_date': '2022',
            'description': 'Led the student body council, organized academic exhibitions and inter-college competitions, and represented the institution in official administrative assemblies.',
            'order': 4
        }
    ]
    for e in exp_data:
        Experience.objects.create(**e)
    print("✅ Experiences Created")

    # 5. Achievements
    Achievement.objects.all().delete()
    ach_data = [
        {
            'title': 'Top 10 Selection & Certificate of Excellence (FYP Exhibition)',
            'issuer': 'UMT School of Systems & Technology (SST)',
            'date': 'July 21, 2026',
            'description': 'Project "Smart Eye: An AI-Driven Traffic Enforcement System" evaluated by internal and external panels among 160+ competing project groups, earning selection into the elite Top 10 tier followed by the prestigious Certificate of Excellence.'
        },
        {
            'title': 'Head Boy Sash & Leadership Honor',
            'issuer': 'APEX Group of Colleges Tajbagh Campus',
            'date': '2022',
            'description': 'Awarded official Head Boy sash and leadership medal for exemplary discipline, academic excellence, and student administration.'
        },
        {
            'title': 'Civic Excellence & Traffic Volunteer Recognition',
            'issuer': 'City Traffic Police Lahore',
            'date': '2025',
            'description': 'Honored for dedication to civic awareness, community traffic guidance, and safety compliance drives.'
        }
    ]
    for a in ach_data:
        Achievement.objects.create(**a)
    print("✅ Achievements Created")

if __name__ == '__main__':
    run()