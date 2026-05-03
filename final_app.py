import streamlit as st
import random
# ─────────────────────────────────────────────
# DATA
# ─────────────────────────────────────────────

CARS = [
    {
        "name": "Ferrari 488 Spider",
        "price_per_day": 1800,
        "tags": ["Sporty", "Luxury"],
        "moods": ["Sporty", "Luxury"],
        "occasions": ["Birthday", "Date", "Wedding"],
        "description": "The Ferrari 488 Spider is a masterpiece of Italian engineering — a mid-engine sports car that converts the highway into a personal racetrack. Its twin-turbocharged V8 screams as the wind rushes through your hair, top-down in theatrical Italian style.",
        "hp": 660, "zero_to_sixty": 3.0, "top_speed": 203,
        "image_url": "https://images.unsplash.com/photo-1592198084033-aade902d1aae?w=1400&q=90",
        "color_accent": "#e8001d",
        "origin": "Maranello, Italy",
        "tagline": "Where passion meets perfection.",
    },
    {
        "name": "Lamborghini Huracán",
        "price_per_day": 2100,
        "tags": ["Sporty", "Fun"],
        "moods": ["Sporty", "Fun"],
        "occasions": ["Birthday", "Casual"],
        "description": "The Huracán is unapologetically dramatic — angular lines, a V10 symphony, and a presence that stops streets cold. This is the car you drive when subtlety is simply not an option.",
        "hp": 630, "zero_to_sixty": 2.9, "top_speed": 202,
        "image_url": "https://images.unsplash.com/photo-1544636331-e26879cd4d9b?w=1400&q=90",
        "color_accent": "#ff6600",
        "origin": "Sant'Agata Bolognese, Italy",
        "tagline": "Born to defy. Built to dominate.",
    },
    {
        "name": "Rolls-Royce Ghost",
        "price_per_day": 2800,
        "tags": ["Luxury", "Romantic"],
        "moods": ["Luxury", "Romantic"],
        "occasions": ["Wedding", "Date", "Birthday"],
        "description": "Inside a Rolls-Royce Ghost, the world outside ceases to exist. Hand-stitched leather, starlight headliner, and a whisper-quiet 6.75L V12 create a sanctuary of unrivalled opulence. This is not a car — it's a statement.",
        "hp": 563, "zero_to_sixty": 4.6, "top_speed": 155,
        "image_url": "https://images.unsplash.com/photo-1631295868223-63265b40d9e4?w=1400&q=90",
        "color_accent": "#c0b283",
        "origin": "Goodwood, England",
        "tagline": "Silence is the loudest luxury.",
    },
    {
        "name": "Porsche 911 Turbo S",
        "price_per_day": 1400,
        "tags": ["Sporty", "Luxury"],
        "moods": ["Sporty", "Luxury"],
        "occasions": ["Casual", "Birthday", "Date"],
        "description": "The 911 Turbo S is the eternal benchmark — a car that does everything better than it has any right to. Precise, powerful, and paradoxically practical, it's a sports car you can actually live with.",
        "hp": 640, "zero_to_sixty": 2.6, "top_speed": 205,
        "image_url": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=1400&q=90",
        "color_accent": "#cc0000",
        "origin": "Stuttgart, Germany",
        "tagline": "Engineered without compromise.",
    },
    {
        "name": "McLaren 720S",
        "price_per_day": 1950,
        "tags": ["Sporty", "Fun"],
        "moods": ["Sporty", "Fun"],
        "occasions": ["Birthday", "Casual"],
        "description": "The McLaren 720S defies physics. Carbon-fiber body, dihedral doors that open skyward, and a twin-turbo V8 that rewrites your understanding of acceleration. This machine was born on the track — and it hasn't forgotten.",
        "hp": 710, "zero_to_sixty": 2.8, "top_speed": 212,
        "image_url": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1400&q=90",
        "color_accent": "#f77f00",
        "origin": "Woking, England",
        "tagline": "The track knows no speed limit.",
    },
    {
        "name": "Audi R8 V10 Plus",
        "price_per_day": 1200,
        "tags": ["Sporty", "Luxury"],
        "moods": ["Sporty", "Luxury", "Fun"],
        "occasions": ["Casual", "Date", "Birthday"],
        "description": "The Audi R8 V10 Plus is everyday exotica — a naturally aspirated V10 that wails at 8,700 RPM, cloaked in sleek German design. Refined enough for a business dinner, raw enough for a mountain road.",
        "hp": 610, "zero_to_sixty": 3.2, "top_speed": 205,
        "image_url": "https://images.unsplash.com/photo-1609521263047-f8f205293f24?w=1400&q=90",
        "color_accent": "#a8090a",
        "origin": "Neckarsulm, Germany",
        "tagline": "Vorsprung durch Thrill.",
    },
    {
        "name": "Bentley Continental GT",
        "price_per_day": 2400,
        "tags": ["Luxury", "Romantic"],
        "moods": ["Luxury", "Romantic"],
        "occasions": ["Wedding", "Date", "Birthday"],
        "description": "The Bentley Continental GT is where art meets engineering. With hand-crafted interiors, a W12 powerplant, and timeless grand tourer proportions, every mile is a curated luxury experience.",
        "hp": 626, "zero_to_sixty": 3.6, "top_speed": 207,
        "image_url": "https://images.unsplash.com/photo-1563720223185-11003d516935?w=1400&q=90",
        "color_accent": "#8b7355",
        "origin": "Crewe, England",
        "tagline": "Effortless power, handcrafted soul.",
    },
    {
        "name": "Mercedes-AMG GT Black Series",
        "price_per_day": 1600,
        "tags": ["Sporty", "Fun"],
        "moods": ["Sporty", "Fun"],
        "occasions": ["Birthday", "Casual"],
        "description": "The AMG GT Black Series is Mercedes at its most unhinged — flat-plane crank V8, massive aero, and a character that borders on racecar. It demands skill and rewards it spectacularly.",
        "hp": 720, "zero_to_sixty": 3.1, "top_speed": 202,
        "image_url": "https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?w=1400&q=90",
        "color_accent": "#cc0000",
        "origin": "Affalterbach, Germany",
        "tagline": "Civilized on the outside. Feral within.",
    },
    {
        "name": "Aston Martin DB11",
        "price_per_day": 1700,
        "tags": ["Luxury", "Romantic"],
        "moods": ["Luxury", "Romantic", "Sporty"],
        "occasions": ["Date", "Wedding", "Birthday"],
        "description": "The Aston Martin DB11 is Bond-level charisma in physical form — sculpted bodywork, twin-turbo V12, and an interior that whispers British aristocracy. Drive it and you become the protagonist.",
        "hp": 600, "zero_to_sixty": 3.7, "top_speed": 200,
        "image_url": "https://images.unsplash.com/photo-1606220945770-b5b6c2c55bf1?w=1400&q=90",
        "color_accent": "#006400",
        "origin": "Gaydon, England",
        "tagline": "The art of being extraordinary.",
    },
    {
        "name": "Ferrari Roma",
        "price_per_day": 1550,
        "tags": ["Luxury", "Romantic"],
        "moods": ["Luxury", "Romantic", "Sporty"],
        "occasions": ["Date", "Wedding", "Birthday"],
        "description": "The Ferrari Roma is la dolce vita on four wheels — elegant, effortless, and intoxicatingly beautiful. Its 620hp V8 is hidden beneath restrained styling that seduces without shouting.",
        "hp": 620, "zero_to_sixty": 3.4, "top_speed": 199,
        "image_url": "https://images.unsplash.com/photo-1583121274602-3e2820c69888?w=1400&q=90",
        "color_accent": "#e8001d",
        "origin": "Maranello, Italy",
        "tagline": "La dolce vita, redefined.",
    },
]


# ─────────────────────────────────────────────
# LOGIC
# ─────────────────────────────────────────────

def score_car(car, budget, mood, occasion):
    score = 0
    score += 10 if car["price_per_day"] <= budget else -(car["price_per_day"] - budget) / 100
    if mood in car["moods"]: score += 8
    if occasion in (car.get("occasions") or []): score += 6
    return score


def recommend_car(budget, mood, occasion):
    scored = sorted([(score_car(c, budget, mood, occasion), c) for c in CARS], key=lambda x: x[0], reverse=True)
    return scored[0][1]


def is_over_budget(car, budget):
    return car["price_per_day"] > budget


def generate_why_fits(car, mood, occasion):
    stories = {
        ("Luxury","Birthday"): f"You didn't just want a car — you wanted a moment that breathes. The {car['name']} doesn't celebrate birthdays; it transforms them. Every detail of this machine echoes your desire for the extraordinary. When the doors close and the engine stirs, that's not a vehicle starting — that's your story beginning.",
        ("Luxury","Date"): f"Some evenings are meant to be remembered forever. You already knew that — which is why we chose the {car['name']} for you. It arrives before you do. The impression is set before a word is spoken. Tonight, the car does the talking. You simply enjoy the silence that follows.",
        ("Luxury","Wedding"): f"Your wedding day deserves an arrival that matches the magnitude of the moment. The {car['name']} carries you not just to the venue — but into the story your guests will retell for years. We chose it because luxury, like love, should never compromise.",
        ("Luxury","Casual"): f"Some days, ordinary is simply not enough. You felt that today — and we agreed. The {car['name']} turns every errand into an occasion, every road into a runway. Life is too short to drive something forgettable.",
        ("Sporty","Birthday"): f"Happy birthday to someone who refuses to slow down. The {car['name']} was built for exactly this energy — relentless, alive, and absolutely unforgettable. Today you don't just celebrate another year. You celebrate the kind of person who chooses a {car['name']}.",
        ("Sporty","Date"): f"You wanted the date to start with an exclamation mark, not a question. Smart. The {car['name']} does that for you — the moment it rolls up, you've already won the evening. Adrenaline and romance share more DNA than people realize.",
        ("Sporty","Casual"): f"You're the kind of person who finds thrill in the ordinary. The {car['name']} respects that completely. No occasion needed. No justification required. Just open road and raw sound.",
        ("Sporty","Wedding"): f"Who said weddings have to be quiet? The {car['name']} gives your entrance a heartbeat — literally. Because you've never done anything the conventional way, and today is no different.",
        ("Fun","Birthday"): f"Birthdays are meant to be loud, fast, and completely over the top. The {car['name']} agrees with you entirely. Forget the candles — this year, you blow the rev limiter instead.",
        ("Fun","Casual"): f"Sometimes the best plan is no plan at all — just a tank of fuel and the right machine. The {car['name']} is exactly that kind of partner. Spontaneous. Spectacular. Unapologetically fun.",
        ("Romantic","Date"): f"Romance lives in the details — and you've already nailed the biggest one. The {car['name']} doesn't just take you somewhere beautiful; it makes the journey the destination. By the time you arrive, the evening has already begun.",
        ("Romantic","Wedding"): f"Love deserves to travel in something worthy of the occasion. The {car['name']} is that something — timelessly beautiful, effortlessly commanding, and built for moments that matter most. Your 'I do' deserves an arrival to match.",
        ("Romantic","Birthday"): f"This birthday isn't about cake and balloons. It's about making someone feel like the most important person in the world — and arriving in a {car['name']} says exactly that, without a single word.",
    }
    return stories.get((mood, occasion),
        f"We didn't just find you a car — we found you the car. The {car['name']} was chosen to honour "
        f"your unique character and ensure this moment becomes the one worth remembering. "
        f"Because here at RevRide, mediocrity was never on the menu.")


def generate_instagram_caption(car, occasion, mood):
    templates = [
        f"Life's too short for ordinary rides. 🖤\n{car['name']} · {car['tagline']}\n#{mood.lower()}life #supercar #RevRideAI #DriveDifferent",
        f"The roads don't deserve this. But I do. 🏎️✨\n#{car['name'].replace(' ','')} #luxury{occasion.lower()} #RevRideAI",
        f"Not all who wander are lost — some are just in a {car['name']} 🔥\n#supercar #{mood.lower()}vibes #RevRide #NoOrdinaryDay",
        f"They said dream big. Nobody mentioned limits. 💛🖤\n{car['name']} · ${car['price_per_day']:,}/day\n#{occasion.lower()}goals #DriveDifferent #RevRideAI",
        f"Some mornings you wake up and choose the extraordinary. 🖤🏎\n{car['name']} · {car['origin']}\n#supercar #{mood.lower()} #RevRideAI",
    ]
    return random.choice(templates)


def generate_experience_plan(car, occasion):
    plans = {
        "Date": [
            ("🌆","The Grand Arrival", f"Pull up to the restaurant in the {car['name']}. Don't rush. Let the valet moment breathe. That pause before you step out — that's the whole opener."),
            ("🛣️","The Coastal Escape", f"After dinner, take the scenic route — windows down, playlist on low. The {car['name']} turns every curve into a conversation."),
            ("🌅","The Viewpoint", "Find your spot on the hilltop before midnight. The city below. The engine ticking as it cools. No filter needed. No words either."),
        ],
        "Birthday": [
            ("🎁","The Reveal", f"Surprise them at sunrise with the {car['name']} waiting outside — engine running, bow optional. Watch their face. That reaction is the gift."),
            ("🏎️","The Open Road", "Find the longest, emptiest stretch of highway you can. Open it up — just once. That sound is the birthday song they actually deserved."),
            ("🥂","The Golden Hour Toast", "End the day at a rooftop bar as the sun goes down. Champagne. The car gleaming below. This is what 'unforgettable birthday' actually means."),
        ],
        "Wedding": [
            ("💍","The Ceremony Arrival", f"Pull up to the venue with five minutes to spare. The {car['name']} parked front and centre. Every guest has their phones out before you even step out."),
            ("📸","The Portrait Session", "Carve out 20 minutes with the photographer. These images — car, couple, golden light — will outlast everything else from today."),
            ("🌙","The Getaway", "Slip away from the reception before the night ends. Just you two, the open road, and the whole rest of your lives ahead. Drive slowly. Savour it."),
        ],
        "Casual": [
            ("☕","The Morning Ritual", f"Start with a strong espresso. Then take the long route — because the {car['name']} deserves better than shortcuts."),
            ("🗺️","No Destination", "Turn off the GPS. Follow instinct and backroads. The best days rarely have a plan — they just have the right machine."),
            ("🌇","The Return", "Come back through the city at golden hour with the windows down. Let them stare. You earned it."),
        ],
    }
    return plans.get(occasion, plans["Casual"])


# ─────────────────────────────────────────────
# STYLES
# ─────────────────────────────────────────────

def inject_global_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=DM+Sans:wght@300;400;500;600&display=swap');

    *, *::before, *::after { box-sizing: border-box; }
    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
        background-color: #080c17;
        color: #e2d9c8;
    }
    .stApp { background: #080c17; }

    /* ── Sidebar ── */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg,#0b0f1c 0%,#0d1220 100%);
        border-right: 1px solid rgba(212,175,55,0.12);
    }
    section[data-testid="stSidebar"] * { color: #e2d9c8 !important; }

    /* ── Slider ── */
    .stSlider > div > div > div > div { background: #d4af37 !important; }
    .stSlider > div > div > div { background: rgba(212,175,55,0.18) !important; }
    .stSlider label, .stSelectbox label {
        color: #d4af37 !important;
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 600 !important; font-size: 0.68rem !important;
        letter-spacing: 0.15em !important; text-transform: uppercase !important;
    }

    /* ── Selectbox ── */
    div[data-baseweb="select"] {
        background: #0f1623 !important;
        border: 1px solid rgba(212,175,55,0.28) !important;
        border-radius: 6px !important;
    }
    div[data-baseweb="select"] * {
        color: #e2d9c8 !important; background: #0f1623 !important;
        font-family: 'DM Sans', sans-serif !important;
    }

    /* ── Button ── */
    .stButton > button {
        background: linear-gradient(135deg,#d4af37 0%,#b8941e 100%);
        color: #080c17; font-family: 'DM Sans', sans-serif;
        font-weight: 700; font-size: 0.78rem; letter-spacing: 0.18em;
        text-transform: uppercase; border: none; border-radius: 4px;
        padding: 0.8rem 1.5rem; width: 100%;
        box-shadow: 0 4px 20px rgba(212,175,55,0.2);
        transition: all 0.25s ease;
    }
    .stButton > button:hover {
        box-shadow: 0 0 32px rgba(212,175,55,0.45);
        transform: translateY(-1px);
    }

    /* ── Tabs ── */
    .stTabs [data-baseweb="tab-list"] {
        background: transparent !important;
        border-bottom: 1px solid rgba(212,175,55,0.13) !important;
        gap: 0; padding: 0 !important;
    }
    .stTabs [data-baseweb="tab"] {
        background: transparent !important; color: #5a5545 !important;
        font-family: 'DM Sans', sans-serif !important; font-size: 0.72rem !important;
        font-weight: 600 !important; letter-spacing: 0.2em !important;
        text-transform: uppercase !important; border: none !important;
        border-bottom: 2px solid transparent !important;
        padding: 0.85rem 1.8rem !important; transition: all 0.2s ease !important;
    }
    .stTabs [aria-selected="true"] {
        color: #d4af37 !important;
        border-bottom: 2px solid #d4af37 !important;
        background: transparent !important;
    }
    .stTabs [data-baseweb="tab-panel"] { padding-top: 0 !important; background: transparent !important; }
    .stTabs [data-baseweb="tab-highlight"] { display: none !important; }

    /* ── Animations ── */
    @keyframes fadeUp {
        from { opacity: 0; transform: translateY(20px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

    .fade-up { animation: fadeUp 0.55s cubic-bezier(0.22,0.61,0.36,1) both; }
    .fade-in { animation: fadeIn 0.5s ease both; }
    .d1 { animation-delay: 0.05s; } .d2 { animation-delay: 0.13s; }
    .d3 { animation-delay: 0.22s; } .d4 { animation-delay: 0.32s; }

    /* ── Gold shimmer on price ── */
    @keyframes shimmer {
        0%   { background-position: -200% center; }
        100% { background-position:  200% center; }
    }
    .price-shimmer {
        background: linear-gradient(90deg,#d4af37 0%,#f5e47a 40%,#d4af37 60%,#a8871d 100%);
        background-size: 200% auto;
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        background-clip: text; animation: shimmer 3.5s linear infinite;
    }

    /* ── Hide Streamlit chrome ── */
#MainMenu, footer { visibility: hidden; } 

/* Remove 'header' from visibility:hidden so the sidebar toggle stays visible */
header[data-testid="stHeader"] {
    background: transparent !important;
    color: #d4af37 !important; /* Makes the toggle button gold to match your theme */
}

.block-container { padding-top: 0.25rem; max-width: 1180px; }
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# COMPONENTS
# ─────────────────────────────────────────────

def render_header():
    st.markdown("""
<div class="fade-in" style="text-align:center; padding:2.2rem 0 1.2rem;">
<div style="font-family:'DM Sans',sans-serif; font-size:0.6rem; font-weight:600;
letter-spacing:0.45em; color:#d4af37; text-transform:uppercase; margin-bottom:0.9rem;">
✦ &nbsp; Exclusive Supercar Experience &nbsp; ✦
</div>
<h1 style="font-family:'Cormorant Garamond',serif; font-size:clamp(2.8rem,6vw,5rem);
font-weight:700; letter-spacing:0.06em; margin:0; line-height:1;
background:linear-gradient(135deg,#d4af37 0%,#f5e47a 45%,#a8871d 100%);
-webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;">
RevRide AI
</h1>
<p style="font-family:'Cormorant Garamond',serif; font-style:italic; font-size:1.1rem;
color:#9a8050; margin-top:0.55rem; letter-spacing:0.1em;">
Don't just dream it. Drive it.
</p>
<div style="width:55px; height:1px; margin:1.2rem auto 0;
background:linear-gradient(90deg,transparent,#d4af37,transparent);"></div>
</div>
    """, unsafe_allow_html=True)


def render_hero(car, over_budget):
    # Determine if the premium badge should be shown
    badge = ""
    if over_budget:
        badge = """<div style="position:absolute;top:18px;right:18px;z-index:10;
            background:rgba(160,20,20,0.82);border:1px solid rgba(239,68,68,0.55);
            color:#fecaca;font-family:'DM Sans',sans-serif;font-size:0.6rem;font-weight:700;
            letter-spacing:0.18em;text-transform:uppercase;padding:0.32rem 0.8rem;border-radius:3px;
            backdrop-filter:blur(6px);">⚠ &nbsp;Slightly Over Budget</div>"""

    # Generate the tag bubbles
    tags_html = "".join([f"""<span style="background:rgba(212,175,55,0.1);border:1px solid rgba(212,175,55,0.38);
        color:#d4af37;font-family:'DM Sans',sans-serif;font-size:0.57rem;font-weight:700;
        letter-spacing:0.22em;text-transform:uppercase;padding:0.25rem 0.7rem;border-radius:2px;
        backdrop-filter:blur(8px);">{t}</span>""" for t in car['tags']])

    # Use a single continuous string for the markdown to prevent accidental code-block formatting
    hero_content = f"""
<div class="fade-in" style="position:relative;border-radius:14px;overflow:hidden;border:1px solid rgba(212,175,55,0.18);box-shadow:0 0 80px rgba(212,175,55,0.06),0 32px 80px rgba(0,0,0,0.7);margin-bottom:0.6rem;">
<img src="{car['image_url']}" style="width:100%;height:490px;object-fit:cover;display:block;filter:brightness(0.52) contrast(1.06);" />
<div style="position:absolute;inset:0;background:linear-gradient(to top,rgba(8,12,23,0.97) 0%,rgba(8,12,23,0.5) 32%,rgba(8,12,23,0.12) 58%,transparent 78%);"></div>
<div style="position:absolute;top:20px;left:22px;font-family:'DM Sans',sans-serif;font-size:0.58rem;font-weight:600;letter-spacing:0.22em;color:rgba(212,175,55,0.75);text-transform:uppercase;">{car['origin']}</div>
{badge}
<div style="position:absolute;bottom:0;left:0;right:0;padding:1.8rem 2.4rem 2.4rem;">
<div style="display:flex;gap:0.5rem;margin-bottom:0.85rem;flex-wrap:wrap;">{tags_html}</div>
<h2 style="font-family:'Cormorant Garamond',serif;font-size:clamp(1.9rem,4.5vw,3.1rem);font-weight:700;color:#fff;margin:0 0 0.15rem;line-height:1.1;">{car['name']}</h2>
<div style="display:flex;align-items:baseline;gap:0.5rem;">
<span class="price-shimmer" style="font-family:'Cormorant Garamond',serif;font-size:2.1rem;font-weight:700;">${car['price_per_day']:,}</span>
</div>
</div>
</div>"""
    
    st.markdown(hero_content, unsafe_allow_html=True)


def render_performance(car):
    stats = [
        ("Horsepower", f"{car['hp']}", "HP", "🏎"),
        ("0 – 60 mph",  f"{car['zero_to_sixty']}s", "seconds", "⚡"),
        ("Top Speed",   f"{car['top_speed']}",       "mph",     "🚀"),
    ]
    cards = "".join([f"""
<div class="fade-up d{i+1}" style="flex:1;text-align:center;padding:1.3rem 0.7rem;
background:linear-gradient(145deg,#0f1623,#0b0f1a);
border:1px solid rgba(212,175,55,0.13);border-radius:10px;position:relative;overflow:hidden;">
<div style="position:absolute;top:0;left:50%;transform:translateX(-50%);
width:36px;height:1px;background:rgba(212,175,55,0.5);"></div>
<div style="font-size:1.2rem;margin-bottom:0.45rem;">{emoji}</div>
<div style="font-family:'Cormorant Garamond',serif;font-size:1.9rem;
font-weight:700;color:#d4af37;line-height:1;">{value}</div>
<div style="font-family:'DM Sans',sans-serif;font-size:0.52rem;color:rgba(110,120,135,0.9);
letter-spacing:0.2em;text-transform:uppercase;margin-top:0.18rem;font-weight:600;">{unit}</div>
<div style="font-family:'DM Sans',sans-serif;font-size:0.57rem;color:rgba(150,140,120,0.55);
letter-spacing:0.12em;text-transform:uppercase;margin-top:0.12rem;">{label}</div>
</div>
    """ for i, (label, value, unit, emoji) in enumerate(stats)])

    st.markdown(f'<div style="display:flex;gap:0.8rem;margin:1rem 0 1.8rem;">{cards}</div>', unsafe_allow_html=True)


def render_card(title, content, icon="✦", delay_cls="d1"):
    st.markdown(f"""
<div class="fade-up {delay_cls}" style="background:linear-gradient(145deg,#0f1623,#0b0f1a);
border:1px solid rgba(212,175,55,0.13);border-radius:12px;
padding:1.7rem 1.9rem;margin-bottom:1.1rem;position:relative;overflow:hidden;">
<div style="position:absolute;top:0;left:0;right:0;height:1px;
background:linear-gradient(90deg,transparent,rgba(212,175,55,0.45),transparent);"></div>
<div style="font-family:'DM Sans',sans-serif;font-size:0.56rem;font-weight:700;
letter-spacing:0.3em;text-transform:uppercase;color:#d4af37;margin-bottom:0.9rem;">
{icon} &nbsp; {title}</div>
<div style="font-family:'DM Sans',sans-serif;font-size:0.91rem;
line-height:1.9;color:rgba(205,195,175,0.85);">{content}</div>
</div>
    """, unsafe_allow_html=True)


def render_why_fits_card(text, delay_cls="d2"):
    st.markdown(f"""
<div class="fade-up {delay_cls}" style="background:linear-gradient(145deg,#111826,#0c1018);
border:1px solid rgba(212,175,55,0.2);border-radius:12px;
padding:1.9rem 2rem;margin-bottom:1.1rem;position:relative;overflow:hidden;">
<div style="position:absolute;top:0;left:0;right:0;height:1px;
background:linear-gradient(90deg,transparent,#d4af37,transparent);"></div>
<div style="position:absolute;bottom:-25px;right:-15px;font-size:5rem;
opacity:0.025;user-select:none;pointer-events:none;">✦</div>
<div style="font-family:'DM Sans',sans-serif;font-size:0.56rem;font-weight:700;
letter-spacing:0.3em;text-transform:uppercase;color:#d4af37;margin-bottom:1.1rem;">
✦ &nbsp; WHY THIS FITS YOU</div>
<p style="font-family:'Cormorant Garamond',serif;font-size:1.1rem;font-style:italic;
line-height:2;color:rgba(220,210,190,0.9);margin:0;">{text}</p>
</div>
    """, unsafe_allow_html=True)


def render_experience_plan(steps, delay_cls="d3"):
    steps_html = "".join([f"""
<div style="display:flex;align-items:flex-start;gap:1.1rem;padding:1rem 0;
border-bottom:1px solid rgba(212,175,55,0.07);">
<div style="min-width:34px;height:34px;border-radius:50%;
background:linear-gradient(135deg,#d4af37,#a8871d);
display:flex;align-items:center;justify-content:center;
font-size:0.95rem;flex-shrink:0;margin-top:2px;
box-shadow:0 0 10px rgba(212,175,55,0.25);">{emoji}</div>
<div>
<div style="font-family:'DM Sans',sans-serif;font-size:0.65rem;font-weight:700;
letter-spacing:0.13em;text-transform:uppercase;color:#d4af37;margin-bottom:0.25rem;">{title}</div>
<div style="font-family:'DM Sans',sans-serif;font-size:0.87rem;
line-height:1.75;color:rgba(195,185,165,0.8);">{desc}</div>
</div>
</div>
    """ for emoji, title, desc in steps])

    st.markdown(f"""
<div class="fade-up {delay_cls}" style="background:linear-gradient(145deg,#0f1623,#0b0f1a);
border:1px solid rgba(212,175,55,0.13);border-radius:12px;
padding:1.7rem 1.9rem;margin-bottom:1.1rem;position:relative;overflow:hidden;">
<div style="position:absolute;top:0;left:0;right:0;height:1px;
background:linear-gradient(90deg,transparent,rgba(212,175,55,0.45),transparent);"></div>
<div style="font-family:'DM Sans',sans-serif;font-size:0.56rem;font-weight:700;
letter-spacing:0.3em;text-transform:uppercase;color:#d4af37;margin-bottom:0.4rem;">
🗺 &nbsp; YOUR EXPERIENCE PLAN</div>
{steps_html}
</div>
    """, unsafe_allow_html=True)


def render_instagram_card(caption, delay_cls="d4"):
    caption_html = caption.replace("\n", "<br>")
    st.markdown(f"""
<div class="fade-up {delay_cls}" style="background:linear-gradient(145deg,#0f1623,#0b0f1a);
border:1px solid rgba(212,175,55,0.13);border-radius:12px;
padding:1.7rem 1.9rem;margin-bottom:1.1rem;position:relative;overflow:hidden;">
<div style="position:absolute;top:0;left:0;right:0;height:1px;
background:linear-gradient(90deg,transparent,rgba(212,175,55,0.45),transparent);"></div>
<div style="font-family:'DM Sans',sans-serif;font-size:0.56rem;font-weight:700;
letter-spacing:0.3em;text-transform:uppercase;color:#d4af37;margin-bottom:1.1rem;">
📸 &nbsp; YOUR INSTAGRAM CAPTION</div>
<div style="background:rgba(212,175,55,0.035);border:1px dashed rgba(212,175,55,0.22);
border-radius:8px;padding:1.3rem 1.5rem;">
<p style="font-family:'Cormorant Garamond',serif;font-style:italic;
font-size:1.03rem;line-height:1.9;color:rgba(220,210,190,0.9);margin:0;">
{caption_html}</p>
</div>
</div>
    """, unsafe_allow_html=True)


def render_budget_warning(car, budget):
    overage = car["price_per_day"] - budget
    st.markdown(f"""
<div class="fade-in" style="background:linear-gradient(135deg,rgba(28,8,8,0.9),rgba(38,10,10,0.9));
border:1px solid rgba(239,68,68,0.28);border-radius:10px;
padding:1.1rem 1.7rem;margin-bottom:1.1rem;display:flex;align-items:flex-start;gap:0.9rem;">
<div style="font-size:1.1rem;margin-top:0.1rem;flex-shrink:0;">⚠️</div>
<div>
<div style="font-family:'DM Sans',sans-serif;font-size:0.56rem;font-weight:700;
letter-spacing:0.2em;text-transform:uppercase;color:#f87171;margin-bottom:0.3rem;">
Premium Notice</div>
<p style="font-family:'DM Sans',sans-serif;font-size:0.87rem;
color:rgba(252,165,165,0.82);margin:0;line-height:1.7;">
This vehicle exceeds your budget by
<strong style="color:#f87171;">${overage:,} per day</strong>.
We believe some experiences are worth stretching for — but the choice is entirely yours.
</p>
</div>
</div>
    """, unsafe_allow_html=True)


def render_divider():
    st.markdown("""
<div style="display:flex;align-items:center;gap:1rem;margin:1.5rem 0;">
<div style="flex:1;height:1px;background:linear-gradient(90deg,transparent,rgba(212,175,55,0.18));"></div>
<div style="color:#d4af37;font-size:0.6rem;letter-spacing:0.3em;opacity:0.5;">✦</div>
<div style="flex:1;height:1px;background:linear-gradient(90deg,rgba(212,175,55,0.18),transparent);"></div>
</div>
    """, unsafe_allow_html=True)


def render_footer():
    st.markdown("""
<div style="text-align:center;padding:2.8rem 0 2rem;
border-top:1px solid rgba(212,175,55,0.09);margin-top:3rem;">
<div style="font-family:'Cormorant Garamond',serif;font-size:1.5rem;font-weight:700;
letter-spacing:0.1em;background:linear-gradient(135deg,#d4af37,#f5e47a,#a8871d);
-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">
RevRide AI</div>
<div style="font-family:'DM Sans',sans-serif;font-size:0.56rem;letter-spacing:0.28em;
color:rgba(70,65,55,0.9);text-transform:uppercase;margin-top:0.45rem;">
Luxury Supercar Experience Platform &nbsp;·&nbsp; Where Passion Meets the Road
</div>
</div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# PAGES
# ─────────────────────────────────────────────

def page_home(budget, mood, occasion, find_clicked):
    if find_clicked or "car" not in st.session_state:
        car = recommend_car(budget, mood, occasion)
        st.session_state.car      = car
        st.session_state.budget   = budget
        st.session_state.mood     = mood
        st.session_state.occasion = occasion
        st.session_state.caption  = generate_instagram_caption(car, occasion, mood)
        st.session_state.steps    = generate_experience_plan(car, occasion)
        st.session_state.why      = generate_why_fits(car, mood, occasion)

    car  = st.session_state.car
    over = is_over_budget(car, st.session_state.budget)

    render_hero(car, over)
    if over:
        render_budget_warning(car, st.session_state.budget)
    render_performance(car)
    render_divider()

    col1, col2 = st.columns([1.05, 0.95], gap="large")
    with col1:
        render_card("The Experience", car["description"], icon="🏎", delay_cls="d1")
        render_instagram_card(st.session_state.caption, delay_cls="d3")
    with col2:
        render_why_fits_card(st.session_state.why, delay_cls="d2")
        render_experience_plan(st.session_state.steps, delay_cls="d4")


def page_about():
    st.markdown("""
<div class="fade-up" style="max-width:800px;margin:2.5rem auto 0;">

<div style="text-align:center;margin-bottom:2.8rem;">
<div style="font-family:'DM Sans',sans-serif;font-size:0.58rem;font-weight:700;
letter-spacing:0.42em;text-transform:uppercase;color:#d4af37;margin-bottom:0.9rem;">
✦ &nbsp; Our Story &nbsp; ✦</div>
<h2 style="font-family:'Cormorant Garamond',serif;font-size:2.7rem;font-weight:700;
color:#e2d9c8;margin:0;line-height:1.15;">From Garage Floors to Living Dreams</h2>
<p style="font-family:'Cormorant Garamond',serif;font-style:italic;
font-size:1.08rem;color:#9a7f4a;margin-top:0.75rem;">
"Why let a masterpiece gather dust when it could fulfill a dream?"</p>
</div>

<div style="background:linear-gradient(145deg,#0f1623,#0b0f1a);
border:1px solid rgba(212,175,55,0.14);border-radius:14px;
padding:2.4rem 2.7rem;margin-bottom:1.3rem;position:relative;overflow:hidden;">
<div style="position:absolute;top:0;left:0;right:0;height:1px;
background:linear-gradient(90deg,transparent,#d4af37,transparent);"></div>
<p style="font-family:'DM Sans',sans-serif;font-size:0.93rem;
line-height:2;color:rgba(205,195,175,0.85);margin:0;">
RevRide AI began with a quiet realization. Growing up in a middle-class family, supercars were the ultimate symbols of "The Big Dream." But from the perspective of an owner, there is a hidden sadness in seeing a high-performance machine sitting idle, losing its mechanical soul to time and neglect.
</p>
<p style="font-family:'DM Sans',sans-serif;font-size:0.93rem;
line-height:2;color:rgba(205,195,175,0.85);margin:1.2rem 0 0;">
We built a bridge between these two worlds. By connecting owners who want to keep their icons in motion with enthusiasts ready to celebrate life’s biggest milestones, we’ve turned luxury into an accessible experience. We ensure that every 'special occasion' has a heartbeat as loud as a V12 engine.
</p>
</div>

<div style="display:flex;gap:1rem;margin-bottom:1.3rem;flex-wrap:wrap;">
<div style="flex:1;min-width:170px;background:linear-gradient(145deg,#0f1623,#0b0f1a);
border:1px solid rgba(212,175,55,0.13);border-radius:12px;padding:1.7rem 1.4rem;text-align:center;">
<div style="font-size:1.6rem;margin-bottom:0.7rem;">🛠️</div>
<div style="font-family:'DM Sans',sans-serif;font-size:0.6rem;font-weight:700;
letter-spacing:0.2em;text-transform:uppercase;color:#d4af37;margin-bottom:0.5rem;">Mechanical Health</div>
<div style="font-family:'DM Sans',sans-serif;font-size:0.8rem;
line-height:1.75;color:rgba(170,160,140,0.8);">Owners generate revenue while ensuring their cars stay road-ready and maintained.</div>
</div>

<div style="flex:1;min-width:170px;background:linear-gradient(145deg,#0f1623,#0b0f1a);
border:1px solid rgba(212,175,55,0.13);border-radius:12px;padding:1.7rem 1.4rem;text-align:center;">
<div style="font-size:1.6rem;margin-bottom:0.7rem;">🥂</div>
<div style="font-family:'DM Sans',sans-serif;font-size:0.6rem;font-weight:700;
letter-spacing:0.2em;text-transform:uppercase;color:#d4af37;margin-bottom:0.5rem;">Event Integration</div>
<div style="font-family:'DM Sans',sans-serif;font-size:0.8rem;
line-height:1.75;color:rgba(170,160,140,0.8);">Bespoke planning that makes supercars the centerpiece of weddings and birthdays.</div>
</div>

<div style="flex:1;min-width:170px;background:linear-gradient(145deg,#0f1623,#0b0f1a);
border:1px solid rgba(212,175,55,0.13);border-radius:12px;padding:1.7rem 1.4rem;text-align:center;">
<div style="font-size:1.6rem;margin-bottom:0.7rem;">🔓</div>
<div style="font-family:'DM Sans',sans-serif;font-size:0.6rem;font-weight:700;
letter-spacing:0.2em;text-transform:uppercase;color:#d4af37;margin-bottom:0.5rem;">Dream Access</div>
<div style="font-family:'DM Sans',sans-serif;font-size:0.8rem;
line-height:1.75;color:rgba(170,160,140,0.8);">Making the extraordinary affordable for the dreamers who value the drive most.</div>
</div>
</div>

<div style="text-align:center;padding:2.4rem;margin-top:0.5rem;
background:linear-gradient(135deg,rgba(212,175,55,0.035),rgba(212,175,55,0.015));
border:1px solid rgba(212,175,55,0.11);border-radius:12px;">
<div style="font-family:'Cormorant Garamond',serif;font-size:1.45rem;
font-style:italic;color:rgba(212,175,55,0.82);line-height:1.65;">
"Driving your dream shouldn't be a lifetime achievement.<br>It should be your next Saturday."
</div>
<div style="font-family:'DM Sans',sans-serif;font-size:0.57rem;font-weight:600;
letter-spacing:0.2em;text-transform:uppercase;color:rgba(140,130,110,0.55);margin-top:1rem;">
— The RevRide Philosophy</div>
</div>

</div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def render_sidebar():
    with st.sidebar:
        st.markdown("""
<div style="padding-top:1.1rem;margin-bottom:1.6rem;">
<div style="font-family:'Cormorant Garamond',serif;font-size:1.28rem;font-weight:700;
background:linear-gradient(135deg,#d4af37,#f5e47a);
-webkit-background-clip:text;-webkit-text-fill-color:transparent;
background-clip:text;letter-spacing:0.08em;margin-bottom:0.12rem;">RevRide AI</div>
<div style="font-family:'DM Sans',sans-serif;font-size:0.52rem;font-weight:600;
letter-spacing:0.3em;text-transform:uppercase;color:rgba(212,175,55,0.42);">
Concierge Configuration</div>
</div>
<div style="width:100%;height:1px;margin-bottom:1.4rem;
background:linear-gradient(90deg,transparent,rgba(212,175,55,0.28),transparent);"></div>
        """, unsafe_allow_html=True)

        budget = st.slider("Daily Budget (USD)", min_value=100, max_value=5000, value=1500, step=50, format="$%d")
        st.markdown("<div style='height:0.3rem'></div>", unsafe_allow_html=True)
        occasion = st.selectbox("Occasion", ["Birthday","Date","Wedding","Casual"])
        st.markdown("<div style='height:0.3rem'></div>", unsafe_allow_html=True)
        mood = st.selectbox("Your Mood", ["Luxury","Sporty","Fun","Romantic"])
        st.markdown("<div style='height:0.9rem'></div>", unsafe_allow_html=True)
        find = st.button("✦  Find My Perfect Car")

        st.markdown(f"""
<div style="margin-top:1.6rem;padding:1.1rem;background:rgba(212,175,55,0.035);
border:1px solid rgba(212,175,55,0.1);border-radius:8px;
font-family:'DM Sans',sans-serif;font-size:0.7rem;
color:rgba(110,105,90,0.9);line-height:1.8;">
Our AI concierge matches your preferences against a curated fleet of the world's finest machines.
</div>
<div style="margin-top:1.4rem;text-align:center;">
<div style="font-family:'DM Sans',sans-serif;font-size:0.52rem;font-weight:600;
letter-spacing:0.25em;text-transform:uppercase;color:rgba(212,175,55,0.28);">
Budget selected</div>
<div style="font-family:'Cormorant Garamond',serif;font-size:1.55rem;
font-weight:700;color:#d4af37;margin-top:0.1rem;">
${budget:,}<span style="font-size:0.78rem;font-weight:400;color:rgba(212,175,55,0.45);">/day</span>
</div>
</div>
        """, unsafe_allow_html=True)

    return budget, mood, occasion, find


def main():
    st.set_page_config(
        page_title="RevRide AI — Luxury Supercar Experience",
        page_icon="🏎",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    inject_global_styles()
    budget, mood, occasion, find_clicked = render_sidebar()
    render_header()

    tab_home, tab_about = st.tabs(["🏎  Experience", "✦  Our Story"])

    with tab_home:
        st.markdown("<div style='height:1.4rem'></div>", unsafe_allow_html=True)
        page_home(budget, mood, occasion, find_clicked)

    with tab_about:
        st.markdown("<div style='height:0.4rem'></div>", unsafe_allow_html=True)
        page_about()

    render_footer()


if __name__ == "__main__":
    main()
