# =========================================================
# EnergyGuard AI – 
# Author: Retina Majumder
# Purpose: Sharp Energy Intelligence & Decision Support
# =========================================================

# ---------------- ENERGY RECORD ----------------
class EnergyRecord:
    def __init__(self, usage, expected_avg, sector, time, sunlight, temperature):
        self.usage = usage
        self.expected_avg = expected_avg
        self.sector = sector
        self.time = time
        self.sunlight = sunlight
        self.temperature = temperature


# ---------------- HISTORY MODULE ----------------
class EnergyHistory:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def trend_average(self):
        if len(self.records) < 2:
            return None
        return sum(r.usage for r in self.records) / len(self.records)


# ---------------- ANALYTICS CORE ----------------
class EnergyAnalytics:

    @staticmethod
    def usage_ratio(record):
        return record.usage / record.expected_avg

    @staticmethod
    def anomaly_detected(record, history):
        if not history.records:
            return False
        last = history.records[-1].usage
        return record.usage > last * 1.25

    @staticmethod
    def alert_level(ratio, anomaly):
        if ratio >= 1.35 or anomaly:
            return "CRITICAL"
        elif ratio >= 1.15:
            return "WARNING"
        return "NORMAL"

    @staticmethod
    def efficiency_score(ratio):
        score = 100 - abs(ratio - 1) * 75
        return round(max(0, min(100, score)), 1)


# ---------------- AI DECISION ENGINE ----------------
class KeenAIBrain:

    def decide(self, record, ratio, anomaly, alert):
        reasons = []
        actions = []
        confidence = 0

        # ---- Cause Analysis ----
        reasons.append(f"Usage is {ratio:.2f}× expected level")

        if anomaly:
            reasons.append("Sudden energy spike detected")

        if record.temperature > 30:
            reasons.append("High temperature → increased cooling demand")
            confidence += 15

        if record.sunlight and record.time == "Day":
            reasons.append("Available sunlight not optimally utilized")
            confidence += 20

        if record.sector == "Factory":
            reasons.append("Industrial processes generate recoverable waste")
            confidence += 20

        if record.sector == "Power Plant":
            reasons.append("Grid-level load balancing opportunity detected")
            confidence += 20

        # ---- Action Logic ----
        if alert == "CRITICAL":
            actions.append(("IMMEDIATE", "Reduce non-essential electrical load"))

            if record.sunlight:
                actions.append(("IMMEDIATE", "Activate Smart Daylight-Mirroring System"))

            if record.sector in ["Factory", "Power Plant"]:
                actions.append(("IMMEDIATE", "Enable ORC Waste Energy Recovery Line"))

            actions.append(("HIGH", "Shift base load to geothermal supply"))

        elif alert == "WARNING":
            actions.append(("MEDIUM", "Optimize operational schedule"))
            if record.sunlight:
                actions.append(("MEDIUM", "Increase daylight-based lighting usage"))

        else:
            actions.append(("LOW", "No corrective action required"))

        confidence = min(100, confidence + 30)
        return reasons, actions, confidence


# ---------------- ALERT DISPLAY ----------------
class AlertDisplay:
    @staticmethod
    def show(alert, score):
        print("\n========== ENERGY STATUS ==========")
        if alert == "CRITICAL":
            print("🔴 CRITICAL – Grid stress detected")
        elif alert == "WARNING":
            print("🟡 WARNING – Inefficiency rising")
        else:
            print("🟢 NORMAL – System balanced")

        print(f"⚡ Efficiency Score: {score}/100")


# ---------------- MAIN SYSTEM ----------------
def main():
    history = EnergyHistory()
    analytics = EnergyAnalytics()
    ai = KeenAIBrain()

    print("\n=== EnergyGuard AI – Keen Edition ===\n")

    usage = float(input("Current energy usage (kWh): "))
    expected = float(input("Expected average usage (kWh): "))
    sector = input("Sector (Home / Factory / Power Plant): ").strip().capitalize()
    time = input("Time (Day/Night): ").strip().capitalize()
    sunlight = input("Sunlight available? (yes/no): ").lower() == "yes"
    temperature = float(input("Ambient temperature (°C): "))

    record = EnergyRecord(
        usage, expected, sector, time, sunlight, temperature
    )

    anomaly = analytics.anomaly_detected(record, history)
    history.add(record)

    ratio = analytics.usage_ratio(record)
    alert = analytics.alert_level(ratio, anomaly)
    score = analytics.efficiency_score(ratio)

    AlertDisplay.show(alert, score)

    reasons, actions, confidence = ai.decide(record, ratio, anomaly, alert)

    print("\n--- AI DIAGNOSIS (CAUSE → IMPACT) ---")
    for r in reasons:
        print("•", r)

    print("\n--- AI ACTION PLAN (PRIORITIZED) ---")
    for level, act in actions:
        print(f"[{level}] {act}")

    print(f"\nAI Decision Confidence: {confidence}%")
    print("\n--- SYSTEM READY FOR NEXT CYCLE ---")


# ---------------- RUN ----------------
if __name__ == "__main__":
    main()
