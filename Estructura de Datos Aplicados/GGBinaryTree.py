"""
Guilty Gear Character Binary Tree with gameplay mechanics

This program organizes key Guilty Gear characters in a binary tree structure,
highlighting their relationships, narrative roles, and gameplay impact up to GG Strive.
"""

class GGCharacter:
    """Node representing a Guilty Gear character with gameplay data"""
    
    def __init__(self, name, role, description, mechanics=None, left=None, right=None):
        """
        Initialize a character node with:
        - name: Character's name
        - role: Their narrative role
        - description: Key character traits
        - mechanics: Dictionary of gameplay mechanics and meta impact
        - left: Connection to left child
        - right: Connection to right child
        """
        self.name = name
        self.role = role
        self.description = description
        self.mechanics = mechanics or {}
        self.left = left
        self.right = right
    
    def __str__(self):
        """Display character information with gameplay impact"""
        mechanics_str = "\n".join(f"- {k}: {v}" for k,v in self.mechanics.items())
        return (f"{self.name} ({self.role})\n"
                f"Description: {self.description}\n"
                f"Gameplay Impact:\n{mechanics_str}")

class GGCharacterTree:
    """Enhanced binary tree with character relationships and gameplay analysis"""
    
    def __init__(self):
        """Initialize tree with Sol Badguy as root"""
        self.root = self._build_character_tree()
    
    def _build_character_tree(self):
        """Construct the character relationship tree with gameplay data"""
        
        # Create all character nodes with their mechanics
        asuka = GGCharacter(
            "Asuka R. Kreutz (That Man)",
            "Central Figure",
            "The mysterious orchestrator of events. Original creator of the Gears.",
            mechanics={
                "Unique Mechanic": "Spell Charges system",
                "Meta Impact": "High execution barrier with spell management. Asuka's defining mechanic are his Spells. Instead of having normal special moves that can be used at any time, Asuka’s special moves are tied to four spell slots, which are managed similarly to a card game. By using Chant, Asuka can fire off a spell, which uses it up and requires Asuka to draw another one with Bookmark. Each spell is drawn at random from a deck of 30 different spells (including duplicates), with the contents changing depending on the deck (called “Test Case”) Asuka currently has activated. Test Case 1 specializes in zoning, Test Case 2 specializes in close-range combat and mixups, and Test Case 3 specializes in pressure and unconventional effects.",
                "Tier Placement": "Top tier in GG Strive (Season 3)"
            }
        )
        
        happy_chaos = GGCharacter(
            "Happy Chaos",
            "Primary Antagonist (GG Strive)",
            "Embodiment of absolute freedom. Formerly the Original.",
            mechanics={
                "Unique Mechanic": "Concentration gauge & gunshots",
                "Meta Impact": "Redefined neutral game in Strive. The Gunslinging Broken Messiah, Happy Chaos is a versatile character who controls space through the usage of his gun and excellent normals. Chaos is able to fire his gun by entering either of his shooting stances, At the Ready or Steady Aim. While in either shooting stance Chaos cannot block without using Cancel Aim. Happy Chaos is at his strongest when using both stances interchangeably, thus requiring a mastery of both. Gunplay requires awareness, however, as firing drains two unique resources: Concentration and Ammo. Happy Chaos is a very difficult character, with unorthodox, technical combos and a multitude of resources to juggle, but he makes up for it by being one of the most rewarding and dominant characters in all of Strive.",
                "Tier Placement": "S+ tier on release (nerfed since)"
            }
        )
        
        dizzy = GGCharacter(
            "Dizzy",
            "Peacekeeper",
            "Gear/Valentine hybrid. Connects Sol, Ky, and the world of Gears.",
            mechanics={
                "Unique Mechanic": "Dual-wing summons",
                "Meta Impact": "Pioneered puppet/zoning hybrid styl. In Rev2, Dizzy is an excellent fit for those who enjoy high mobility, long reaching normals, and setplay. She has a great amount of depth and is rewarding to master. Dizzy plays a ""neutral mixup"" game between hitting opponents trying to get in, waiting, summoning with or without meter, movement, and going in. Dizzy has much to offer for veterans and newcomers alike! Playing Dizzy optimally means learning many okizeme setups that depend on character wakeup timings and reversals. Some of Dizzy's setups are difficult to execute and punishing if failed. For newcomers Dizzy has very easy meterless bread and butter combos and can do simple and effective oki. In Strive, Dizzy is a setplay/zoning hybrid character who excels at mid-range pressure and controlling the screen with far reaching moves and projectiles. With her unique ability to freeze opponents, Dizzy can deal massive damage from combo routes that are both easily accessible and possess a lot of depth and nuance.",
                "Tier Placement": "Consistent high-tier in XX/AC+R, her current placement in Strive is still in discussion"
            }
        )
        
        sin = GGCharacter(
            "Sin Kiske",
            "Next Generation",
            "Son of Ky and Dizzy. Represents hope for the future.",
            mechanics={
                "Unique Mechanic": "Stamina gauge for specials",
                "Meta Impact": "Resource management archetype. In Rev2, Sin is a neutral-focused monster with a frighteningly high damage output thanks to his Calorie ""(food)"" gauge which lets him cancel all his special attacks into other special moves. However, if Sin tries to do any special attack with an empty food gauge, he'll be forced into a starving animation that gives his opponent a giant punish. If Sin doesn't find a good chance to eat, he'll often have to give up okizeme or pressure just to refill his food. In Strive, Sin Kiske is a balanced rushdown character, with a lot of similarities to his father Ky. He has an emphasis on long-range normal attacks, neutral-skipping specials, and strong frame trap/mix-up tools. However, he is limited by his resource, Stamina. As long as Sin has Stamina, he can cancel his offensive special moves into their follow-ups, which can deal extra damage, frame trap, and improve his frame data on block, or into Gazelle Step, a lightning fast dash that quickly closes the space between him and his opponent. In addition, Stamina is also very important for combos, allowing Sin to convert good hits into long combos with great corner carry, and even allowing weaker hits to combo into Tyrant Barrel or R.T.L for improved damage, oki, and a likely wallbreak.However, this means that when he is without Stamina, Sin's options are far more limited. He loses access to many of his pressure options, his specials can be punished without the fear of a frame trap, and his reward on hit is reduced dramatically. Playing Sin requires one to be considerate of when to push their advantage, and when to back off and give themselves time to recover. ",
                "Tier Placement": "High-tier in Xrd, rising in Strive"
                }
        )
        
        ky = GGCharacter(
            "Ky Kiske",
            "Deuteragonist",
            "King of Illyria. Sol's rival turned ally. Represents order.",
            mechanics={
                "Unique Mechanic": "Dragon Install (Xrd+)",
                "Meta Impact": "Fundamental shoto template. In all of the Guilty Gear games, Ky Kiske is a well-rounded character with a low barrier to entry. He excels at playing neutral, converting pokes into knockdowns, setting up safe okizeme, and creating strong pressure.",
                "Tier Placement": "Always viable, often top 10"
            },
            left=dizzy,
            right=sin
        )
        
        sol = GGCharacter(
            "Sol Badguy (Frederick)",
            "Protagonist",
            "Former Gear. Seeks to end the cycle of violence. Asuka's first success.",
            mechanics={
                "Unique Mechanic": "Bandit Revolver/Gun Flame",
                "Meta Impact": "Defined rushdown archetype. Sol is a character who excels up close and personal, giving up a little bit of power in the neutral game for a suite of threatening options to open up your opponents during his offense and reward proper conditioning of your opponent. Sol's tricky special moves help him take the risks required to make his way in, and he has a tool-kit of normal moves that allow him to stand his ground and set-up frame traps and strike throw/mix-ups. With ferocious pressure, strong defense, versatile special moves and explosive power, this badass bounty hunter is armed with everything an offensively oriented player could ask for.",
                "Tier Placement": "Top tier in every game (often #1)"
            },
            left=ky,
            right=asuka
        )
        
        # Connect antagonists
        asuka.left = happy_chaos
        
        return sol
    
    def find_character(self, name, current=None):
        """
        Search for a character by name (case-insensitive partial match)
        Returns character node with full gameplay data if found
        """
        if current is None:
            current = self.root
        
        if current.name.lower().startswith(name.lower()):
            return current
        
        found = None
        if current.left:
            found = self.find_character(name, current.left)
        if not found and current.right:
            found = self.find_character(name, current.right)
        
        return found
    
    def print_character_web(self, node=None, level=0):
        """Print character relationships with visual indentation"""
        if node is None:
            node = self.root
        
        print("  " * level + "└─", node.name)
        if node.left or node.right:
            if node.left:
                self.print_character_web(node.left, level + 1)
            if node.right:
                self.print_character_web(node.right, level + 1)
    
    def get_mechanics_report(self, character_name):
        """
        Generate a detailed gameplay impact report for a character
        Returns formatted string with mechanics analysis
        """
        char = self.find_character(character_name)
        if not char:
            return f"Character '{character_name}' not found."
        
        report = [
            f"=== {char.name.upper()} GAMEPLAY ANALYSIS ===",
            f"Role: {char.role}",
            f"Narrative: {char.description}",
            "\nKEY MECHANICS:"
        ]
        
        for mechanic, desc in char.mechanics.items():
            report.append(f"  {mechanic}: {desc}")
        
        return "\n".join(report)

def main():
    """Demonstrate enhanced character tree with gameplay analysis"""
    
    gg_tree = GGCharacterTree()
    
    print("Guilty Gear Core Character Relationships:")
    gg_tree.print_character_web()
    print("\n")
    
    # Gameplay impact analysis
    characters_to_analyze = [
        "Sol",
        "Ky Kiske",
        "Dizzy",
        "Sin Kiske",
        "Asuka",
        "Happy Chaos",
        "Baiken"  # Not in tree
    ]
    
    for name in characters_to_analyze:
        print(gg_tree.get_mechanics_report(name))
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()