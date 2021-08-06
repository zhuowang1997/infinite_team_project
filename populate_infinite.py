import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                    'infinite_team_project.settings')

import django
django.setup()
from infinite.models import Category, Game

def populate():
    Action_Adventure = [
        {'name': 'A Plague Tale: Innocence',
        'likes':0,
        'released_date':'2019-05-15',
        'description':'Follow the critically acclaimed tale of young Amicia and her little brother Hugo, in a heartrending journey through the darkest hours of history.',
        'picture':'./images/Plague.jpg'},
        {'name': 'ARK: Survival Evolved',
        'likes':0,
        'released_date':'2015-06-12',
        'description':'Combining the base game with 3 massive Expansion Packs, ARK: Survival Evolved Explorer\'s Edition is the ultimate way to get even more dinosaur action! The Explorer\'s Edition gives you access to the mega hit ARK: Survival Evolved as well as the Scorched Earth, Aberration, and Extinction Expansion Packs, adding nearly 900 hours of gameplay!',
        'picture':'./images/AFK.jpg'},
        {'name': 'Control',
        'likes':0,
        'released_date':'2020-08-27',
        'description':'After a secretive agency in New York is invaded by an otherworldly threat, you become the new Director struggling to regain Control. From developer Remedy Entertainment, this supernatural 3rd person action-adventure will challenge you to master the combination of supernatural abilities, modifiable loadouts, and reactive environments while fighting through a deep and unpredictable world.',
        'picture':'./images/control.jpg'},
        {'name': 'DayZ',
        'likes':0,
        'released_date':'2013-12-17',
        'description':'The post-soviet country of Chernarus is struck by an unknown virus, turning the majority population into frenzied infected. Fighting over resources has bred a hostile mentality among survivors, driving what’s left of humanity to collapse. You are one of the few immune to the virus - how far will you go to survive?',
        'picture':'./images/dayz.jpg'},
        {'name': 'Dishonored 2',
        'likes':0,
        'released_date':'2016-11-11',
        'description':'Reprise your role as a supernatural assassin in Dishonored 2 – the follow up to Arkane Studio\'s first-person action blockbuster and winner of more than 100 \'Game of the Year\' awards, Dishonored. Play your way in a world where mysticism and industry collide. How will you combine your character\'s unique set of powers, weapons and gadgets to eliminate your enemies?',
        'picture':'./images/Dishonored.jpg'},]

    Simulation = [
        {'name': 'Cities: Skylines',
        'likes':0,
        'released_date':'2017-04-21',
        'description':'Cities: Skylines – Xbox One Edition puts you in charge of a growing city – from the ground-breaking of its first streets to the ever-changing needs of thousands of citizens. Design, build, and manage the city of your dreams, from public services to civic policies, and challenge yourself to grow from a simple town to a bustling metropolitan hub.',
        'picture':'./images/Cities.jpg'},
        {'name': 'Frostpunk',
        'likes':0,
        'released_date':'2018-04-24',
        'description':'Frostpunk is a society survival game where heat means life and every decision comes at a price. Adapted for consoles with revised controls and adjusted mechanics, Frostpunk: Console Edition allows you to fully test your tactical prowess on the frozen wastelands.',
        'picture':'./images/Frostpunk.jpg'},
        {'name': 'Jurassic World Evolution',
        'likes':0,
        'released_date':'2018-06-12',
        'description':'Place yourself at the heart of the Jurassic franchise and build your own Jurassic World. Bioengineer dinosaurs that think, feel and react intelligently to the world around them and face threats posed by espionage, breakouts and devastating tropical storms in an uncertain world where life always finds a way.',
        'picture':'./images/Jurassic.jpg'},
        {'name': 'Football Manager 2021',
        'likes':0,
        'released_date':'2020-11-24',
        'description':'Football Manager 2021 Xbox Edition brings the depth, detail, and drama of the world’s favourite football management simulation series to Xbox. Experience the closest thing to being a real manager by taking charge of the world’s greatest football teams and playing the beautiful game your way. FM21 Xbox achieves football authenticity that other management games can only aspire to. Based on FM Touch, FM21 Xbox is fully optimised for victory with the Xbox Controller for Series X|S and Xbox One.',
        'picture':'./images/football.jpg'},        
        {'name': 'The Sims 4',
        'likes':0,
        'released_date':'2014-09-02',
        'description':'Unleash your imagination and create a unique world of Sims that’s an expression of you! Explore and customize every detail from Sims to homes, and much more. Choose how Sims look, act, and dress, then build and design their incredible homes.',
        'picture':'./images/sim.jpg'},]

    Shooter = [
        {'name': 'Destiny 2',
        'likes':0,
        'released_date':'2019-10-01',
        'description':'Dive into the free-to-play world of Destiny 2 to experience responsive FPS combat, explore the mysteries of our solar system, customize your guardian with unique gear, and unleash elemental abilities against powerful enemies.',
        'picture':'./images/destiny2.jpg'},
        {'name': 'Sniper Elite 4',
        'likes':0,
        'released_date':'2017-02-14',
        'description':'Discover unrivalled sniping freedom in the largest and most advanced World War 2 shooter ever built. Experience tactical third-person combat, gameplay choice and epic longshots across gigantic levels as you liberate wartime Italy from the grip of Fascism. Sniper Elite 4 includes an expansive campaign for 1-2 players, dedicated co-op modes for 2-4 players and gripping competitive multiplayer for up to 12.',
        'picture':'./images/sniper elite4.jpg'},
        {'name': 'Titanfall 2',
        'likes':0,
        'released_date':'2016-10-28',
        'description':'From Respawn Entertainment comes Titanfall® 2. Featuring the debut of a singleplayer campaign and a deeper multiplayer experience, Titanfall® 2 delivers more of the innovative, fast, fluid gameplay fans expect from the series.',
        'picture':'./images/titanfall2.jpg'},
        {'name': 'Halo 5: Guardians',
        'likes':0,
        'released_date':'2015-10-27',
        'description':'Halo 5: Guardians delivers epic multiplayer experiences that span multiple modes, full-featured level building tools, and the most dramatic Halo story to date. With multiple massive FREE content releases since launch, Halo 5: Guardians offers more content, more multiplayer mayhem, and more variety than any Halo ever released! *Online multiplayer requires Xbox Live Gold membership (sold separately)',
        'picture':'./images/halo5.jpg'},
        {'name': 'World of Tanks',
        'likes':0,
        'released_date':'2011-03-15',
        'description':'World of Tanks (WoT) is a massively multiplayer online game developed by Belarusian company Wargaming, featuring 20th century (1910s–1970s) era combat vehicles. It is built upon a freemium business model where the game is free-to-play, but participants also have the option of paying a fee for use of "premium" features. The focus is on player vs. player gameplay with each player controlling an armored vehicle, from the time of Pre-WW2, to the Cold War-era.',
        'picture':'./images/worldoftanks.jpg'}, ]

    Role_playing = [
        {'name': 'NieR: Automata',
        'likes':0,
        'released_date':'2017-03-17',
        'description':'Invaders from another world attack without warning - unleashing the machine lifeforms. To break the deadlock, a new breed of android infantry is sent into the fray: the YoRHa squad. Highly-acclaimed and award winning NieR:Automata™ is a fresh take on the action role-playing game (RPG) genre that gracefully blends mesmerizing action with a captivating story.',
        'picture':'./images/nier_automata.jpg'},
        {'name': 'Octopath Traveler',
        'likes':0,
        'released_date':'2020-04-28',
        'description':'Eight travelers. Eight adventures. Eight roles to play. Embark on an epic journey across the vast and wondrous world of Orsterra and discover the captivating stories of each of the eight travelers.',
        'picture':'./images/octopath.jpg'},
        {'name': 'The Elder Scrolls V: Skyrim Special Edition',
        'likes':0,
        'released_date':'2016-10-28',
        'description':'Winner of more than 200 Game of the Year Awards, the Skyrim Special Edition includes the game and add-ons with all-new features like remastered art and effects, volumetric god rays, dynamic depth of field, and more. Also bring the power of mods to consoles. New quests, environments, characters, dialogue, armor, weapons and more – with Mods, there are no limits to what you can experience.',
        'picture':'./images/elder scrolls.jpg'},
        {'name': 'No Man\'s Sky',
        'likes':0,
        'released_date':'2016-08-09',
        'description':'No Man\'s Sky is a science fiction game about exploration and survival in an infinite procedurally generated universe.',
        'picture':'./images/No mans sky.jpg'},
        {'name': 'Yakuza: Like a Dragon',
        'likes':0,
        'released_date':'2020-11-10',
        'description':'Become Ichiban Kasuga, a low-ranking yakuza grunt left on the brink of death by the man he trusted most. Take up your legendary bat and get ready to crack some underworld skulls in dynamic RPG combat set against the backdrop of modern-day Japan in Yakuza: Like a Dragon. Russian and Brazilian Portuguese subtitles available in early 2021 via patch update. Game leverages Smart Delivery allowing access to both the Xbox One title and Xbox Series X|S title when available.',
        'picture':'./images/Yakuza-Like-a-Dragon.jpg'}, ]

    Real_Time_Strategy = [
        {'name': 'Total War: WARHAMMER II',
        'likes':0,
        'released_date':'2017-09-28',
        'description':'The game\'s announced races in the campaign include the Lizardmen, High Elves, Dark Elves and Skaven. The Tomb Kings and Vampire Coast debuted later as paid downloadable content factions, along with The Huntsmarshal\'s Expedition, the Chevaliers de Lyonesse, and the Sisters of Twilight. The main campaign of the game is called Eye of the Vortex. It is a narrative-focused campaign where each of the playable races has its own story and cutscenes.',
        'picture':'./images/warhammer2.jpg'},
        {'name': 'Wargame: Red Dragon',
        'likes':0,
        'released_date':'2014-04-17',
        'description':'The game is set in East Asia during an alternate history Cold War where the Soviet Union doesn\'t collapse and featuring five new Asia Pacific factions: China, North Korea, South Korea, Japan and the ANZAC. The battlefield is viewed from a top-down perspective. The player can decide which units they want to deploy before a battle, creating a deck of specific individual units from infantry, various forms of armored units, air forces, and naval forces, with further customization available.',
        'picture':'./images/Red dragon.jpg'},
        {'name': 'StarCraft II',
        'likes':0,
        'released_date':'2010-07-27',
        'description':'Wings of Liberty is set four years after the events of StarCraft: Brood War, and focuses on the conflict between Jim Raynor and Arcturus Mengsk. In Heart of the Swarm, the Dominion attacks Raynor and Kerrigan, and the story mainly follows the exploits of Kerrigan, against Mengsk as well as new Protoss-Zerg hybrids.In Legacy of the Void, the Protoss are the protagonists, led by Zeratul and Artanis, fighting against the architect of the Protoss-Zerg hybrids, the evil Amon.',
        'picture':'./images/Starcraft2.jpg'},
        {'name': 'Company of Heroes 2',
        'likes':0,
        'released_date':'2013-06-25',
        'description':'As with the original Company of Heroes, the game is set in World War II but with the focus on the Eastern Front, with players primarily controlling the side of the Soviet Red Army during various stages of the Eastern Front, from Operation Barbarossa to the Battle of Berlin.',
        'picture':'./images/Company of Heroes.jpg'},
        {'name': 'Stellaris',
        'likes':0,
        'released_date':'2016-05-09',
        'description':'Players play as a government of a species in early stages of interstellar space exploration, right after the invention of faster-than-light (FTL) space travel technology. Depending on several factors, such as the ethics of the civilization and the player\'s desires, the ultimate goal of the empire can range from galactic conquest, hoarding of resources and technological supremacy, to peaceful coexistence with or absolute destruction of all other sapient life. ',
        'picture':'./images/Stellaris.jpg'}, ]

    categories = {'Action & adventure': {'name': Action_Adventure},
        'Simulation': {'name': Simulation},
        'Shooter': {'name': Shooter},
        'Role playing': {'name': Role_playing},
        'Real Time Strategy': {'name': Real_Time_Strategy}}

    for category, category_data in categories.items():
        c = add_category(category)
        for p in category_data['name']:
            add_game(c, p['name'], p['released_date'],p['description'],p['picture'],p['likes'])

    for c in Category.objects.all():
        for p in Game.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_game(category, name,released_date,description,picture,likes=0):
    p = Game.objects.get_or_create(category=category, name=name)[0]
    p.description=description
    p.picture=picture
    p.likes=likes
    p.released_date=released_date
    p.save()
    return p

def add_category(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

if __name__ == '__main__':
    print('Starting infinite population script...')
    populate()
