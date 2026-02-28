🏗️ Tradchat 3: The Assembly Line
Welcome to the next generation of our community. Tradchat 3 isn't just a chat app; it’s a modular "Guild" system built for high-trust, high-quality interaction.

🌟 The Vision
A stable, "bubbly," and secure home base. We prioritize human connection over "doom-scrolling" and safety over rapid growth.

👥 The Team
Executives (Athan/Anthony): Vision, Pace, and Gadget-finding.

Designers (Paul/Julianne): Aesthetics, Color Theory, and the "Bubbly" Vibe.

Engineers (Benj/Séamus/Chris): Skeleton, Heartbeat, and Quality Control.

Project Lead (Michael): Systems Architecture and AI-Integration.

🎨 The Design System
We don't do "Dark Sci-Fi" or "Discord Grinders." We do Creamy and Organic.

Master Styles: Found in static/tradchat.css.

Button Types: - .btn-sharp: Serious/Technical.

.btn-soft: Modern/Professional (8px radius).

.btn-bubbly: Friendly/Playful (25px radius).

Dynamic Themes: Every theme is a folder in /static/themes/ containing a background.png and a colors.txt (Python dictionary format).

🛠️ The Tech Stack
Backend: Python + Flask (The Brain).

Database: SQLite3 (The Filing Cabinet).

Real-time: Flask-SocketIO (The Nervous System).

Frontend: HTML5 / CSS3 (The Skin).

🛡️ Security: The Human Gatekeeper
Tradchat 3 has zero direct signups. 1. User submits a request form.
2. User undergoes a Video Verification Call with an Admin.
3. Admin manually creates the account.
4. Users are segregated by age (Under 18 and 18+) into different "Worlds" that never cross.

🚀 The Development "Assembly Line"
To keep the team flowing without burnout:

The Spark: Executives define a feature goal.

The Sketch: Designers create a wireframe/layout.

The Draft: AI generates a "Rough" HTML/CSS version.

The Polish: Engineers clean the code, add comments, and fix the "AI Slop."

The Wire-up: Backend connects the buttons to the database/sockets.

📂 Project Structure
Plaintext
/tradchat3
├── app.py              # Flask Server & Socket Logic
├── database.db         # SQLite Database
├── static/
│   ├── tradchat.css    # MASTER DESIGN SYSTEM
│   ├── themes/         # Theme Folders (bg + colors)
│   └── uploads/        # User-uploaded content
└── templates/
    ├── base.html       # The Global Template
    └── welcome.html    # The Landing Page
"Build it like a crane, live in it like a home." — The Tradchat 3 Motto