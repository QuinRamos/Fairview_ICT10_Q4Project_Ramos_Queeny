from pyscript import document

photos = [
    {
        "name": "Ebtisam ALHAZMI",
        "description": "Glee Club SY 2025-2026",
        "image": "alhazmi.png"
    },
    {
        "name": "Aeiou ALVAREZ",
        "description": "Ped Xing XVII 'Best Bill' Second Place | PPSF Contestant",
        "image": "alvarez.png"
    },
    {
        "name": "Ethan BELSA",
        "description": "ECO SY 2024-2025 | Illuminate Volleyball Camp",
        "image": "belsa.png"
    },
    {
        "name": "Giana BERNAS",
        "description": "Secretary SY 2025-2026 | Science Club SY 2025-2026",
        "image": "bernas.png"
    },
    {
        "name": "Julianna CALAYCAY",
        "description": "Science Club SY 2025-2026",
        "image": "calaycay.png"
    },
    {
        "name": "Jamie CASTELO",
        "description": "Volleyball Varsity SY 2025-2026 | Intrams Green Hornets SY 2025-2026",
        "image": "castelo.png"
    },
    {
        "name": "Meyer CRUZ",
        "description": "Dance Club SY 2024-2026",
        "image": "cruz.png"
    },
    {
        "name": "Ely DEFENSOR",
        "description": "10 Ruby SY 2025-2026",
        "image": "defensor.png"
    },
    {
        "name": "Luna DIMASUHID",
        "description": "Glee Club SY 2022-2026",
        "image": "dimasuhid.png"
    },
    {
        "name": "Mauri FRANCISCO",
        "description": "Dance Club SY 2024-2025 | JCO SY 2025-2026",
        "image": "francisco.png"
    },
    {
        "name": "Cristina HSU",
        "description": "Dance Club SY 2024-2025",
        "image": "hsu.png"
    },
    {
        "name": "Denise JUATCHON",
        "description": "10 Ruby SY 2025-2026",
        "image": "juatchon.png"
    },
    {
        "name": "Judah JUDGE",
        "description": "10 Ruby SY 2025-2026",
        "image": "judge.png"
    },
    {
        "name": "Francis LILAGAN",
        "description": "Treasurer SY 2024-2026 | UST HUMMS Passer",
        "image": "lilagan.png"
    },
    {
        "name": "Sam LUNA",
        "description": "Mayor SY 2024-2026 | Volleyball Varsity SY 2025-2026 | TIMO 2025 Gold Medal Award | PPSF Contestant",
        "image": "luna.png"
    },
    {
        "name": "Enzo MACARANAS",
        "description": "Dance Club SY 2025-2026 | 7th Xavier MUN",
        "image": "macaranas.png"
    },
    {
        "name": "Pain MATEO",
        "description": "Marching Band SY 2024-2026",
        "image": "mateo.png"
    },
    {
        "name": "Ashley MONDRAGON",
        "description": "Marching Band SY 2024-2026",
        "image": "mondragon.png"
    },
    {
        "name": "Lance NALDOZA",
        "description": "Math Club SY 2025-2026",
        "image": "naldoza.png"
    },
    {
        "name": "Gabriel NATIVIDAD",
        "description": "ECO SY 2025-2026",
        "image": "natividad.png"
    },
    {
        "name": "Sofia NG",
        "description": "Science Club SY 2025-2026",
        "image": "ng.png"
    },
    {
        "name": "Hendrich ONG",
        "description": "JCO SY 2025-2026",
        "image": "ong.png"
    },
    {
        "name": "Trisha PAZ",
        "description": "Rank 3 in SS 2Q",
        "image": "paz.png"
    },
    {
        "name": "Miguel RAMOS",
        "description": "Glee Club SY 2024-2026 | Home for the aged volunteer",
        "image": "ramosm.png"
    },
    {
        "name": "Queeny RAMOS",
        "description": "Vice Mayor SY 2024-2026 | CAC SY 2024-2026 | Glee Club SY 2023-2026 | Dance Club SY 2024-2025 | Top Grade and Exam in SS 3Q | Photo Essay Contestant | PPSF Contestant",
        "image": "ramosq.png"
    },
    {
        "name": "Samantha RAMOS",
        "description": "Math Club SY 2025-2026 | Volleyball Varsity SY 2025-2026 | PhiMO Gold Award | DLSU, FEU, MAPUA Passer",
        "image": "ramoss.png"
    },
    {
        "name": "Ashlei REODICA",
        "description": "Intrams Green Hornets SY 2025-2026",
        "image": "reodica.png"
    },
    {
        "name": "Vaughn REPOLONA",
        "description": "Photo Essay Contestant",
        "image": "repolona.png"
    }
]

def show_gallery(event=None):

    gallery = document.getElementById("gallery")

    html = ""

    for person in photos:
        html += f"""
        <div class="card">
            <img src="{person['image']}">
            <div class="card-info">
                <h3>{person['name']}</h3>
                <p>{person['description']}</p>
            </div>
        </div>
        """

    gallery.innerHTML = html


show_gallery()