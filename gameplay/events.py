events = {
    "Grass and Mud": {
        1: "In the Garden",
        2: "In the Garden",
        3: "A Knock at the Door",
        4: "A Knock at the Door",
        5: "The World Gets Darker",
        6: "The World Gets Darker",
    },
    "In the Garden": {
        1: {
            "description": "You happily root about all day in your garden.",
            "outcomes": [
                {
                    "magnitude": 1,
                    "stat": "potatoes",
                },
            ],
        },
        2: {
            "description": "You narrowly avoid a visitor by hiding in a potato sack.",
            "outcomes": [
                {
                    "magnitude": 1,
                    "stat": "potatoes",
                },
                {
                    "magnitude": 1,
                    "stat": "destiny",
                },
            ],
        },
        3: {
            "description": "A hooded stranger lingers outside your farm.",
            "outcomes": [
                {
                    "magnitude": 1,
                    "stat": "destiny",
                },
                {
                    "magnitude": 1,
                    "stat": "orcs",
                },
            ],
        },
        4: {
            "description": "Your field is ravaged in the night by unseen enemies.",
            "outcomes": [
                {
                    "magnitude": 1,
                    "stat": "orcs",
                },
                {
                    "magnitude": -1,
                    "stat": "potatoes",
                },
            ],
        },
        5: {
            "description": "You trade potatoes for other delicious foodstuffs.",
            "outcomes": [
                {
                    "magnitude": -1,
                    "stat": "potatoes",
                },
            ],
        },
        6: {
            "description": "You burrow into a bumper crop of potatoes. Do you cry with joy? Possibly.",
            "outcomes": [
                {
                    "magnitude": 2,
                    "stat": "potatoes",
                },
            ],
        },
    },
    "A Knock at the Door": {
        1: {
            "description": "A distant cousin. They are after your potatoes. They may snitch on you.",
            "outcomes": [
                {
                    "magnitude": 1,
                    "stat": "orcs",
                },
            ],
        },
        2: {
            "description": "A dwarven stranger. You refuse them entry. Ghastly creatures.",
            "outcomes": [
                {
                    "magnitude": 1,
                    "stat": "destiny",
                },
            ],
        },
        3: {
            "description": "A wizard strolls by. You pointedly draw the curtains.",
            "outcomes": [
                {
                    "magnitude": 1,
                    "stat": "orcs",
                },
                {
                    "magnitude": 1,
                    "stat": "destiny",
                },
            ],
        },
        4: {
            "description": "There are rumors of war in the reaches. You eat some potatoes.",
            "outcomes": [
                {
                    "magnitude": -1,
                    "stat": "potatoes",
                },
                {
                    "magnitude": 2,
                    "stat": "orcs",
                },
            ],
        },
        5: {
            "description": "It's an elf. They are not serious people.",
            "outcomes": [
                {
                    "magnitude": 1,
                    "stat": "destiny",
                },
            ],
        },
        6: {
            "description": "It's a sack of potatoes from a generous neighbor. You really must remember to pay them a visit one of these years.",
            "outcomes": [
                {
                    "magnitude": 2,
                    "stat": "potatoes",
                },
            ],
        },
    },
}