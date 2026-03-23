class HUD:
    def __init__(self):
        self.score = 0
        self.health = 100
        self.energy = 100
        self.level = 1
        self.ability_cooldowns = {}
        self.event_logs = []

    def display_score(self):
        print(f"Score: {self.score}")

    def display_health(self):
        print(f"Health: {self.health}")

    def display_energy(self):
        print(f"Energy: {self.energy}")

    def display_level(self):
        print(f"Level: {self.level}")

    def update_ability_cooldown(self, ability_name, cooldown_time):
        self.ability_cooldowns[ability_name] = cooldown_time

    def display_ability_cooldowns(self):
        for ability, time in self.ability_cooldowns.items():
            print(f"{ability} Cooldown: {time} seconds")

    def log_event(self, event):
        self.event_logs.append(event)
        print(f"Event Log: {event}")

    def display_event_logs(self):
        for event in self.event_logs:
            print(f"Event: {event}")
