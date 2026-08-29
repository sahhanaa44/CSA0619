# Q36 - Smart Agriculture Irrigation Optimization
# Greedy Scheduling Algorithm

def calculate_priority(field):
    """
    Calculate priority score based on:
    - Soil moisture deficit
    - Crop priority
    - Deadline urgency
    - Weather condition
    """

    moisture_deficit = 100 - field["soil_moisture"]

    # Higher urgency for earlier deadlines
    deadline_score = 6 - field["deadline"]

    # Weather adjustment
    if field["weather"].lower() == "rain":
        weather_penalty = 5
    elif field["weather"].lower() == "cloudy":
        weather_penalty = 2
    else:
        weather_penalty = 0

    score = (
        moisture_deficit * 0.1
        + field["crop_priority"]
        + deadline_score
        - weather_penalty
    )

    return round(score, 2)


def greedy_irrigation_schedule(fields, available_water):
    """
    Greedy approach:
    1. Calculate priority for every field.
    2. Sort fields by priority in descending order.
    3. Schedule the highest-priority fields first.
    4. Stop when available water is insufficient.
    """

    # Calculate priority score
    for field in fields:
        field["priority_score"] = calculate_priority(field)

    # Greedy sorting
    fields.sort(
        key=lambda x: (
            -x["priority_score"],
            x["deadline"]
        )
    )

    scheduled = []
    skipped = []
    remaining_water = available_water
    slot = 1

    for field in fields:

        # Do not irrigate if rain is expected
        if field["weather"].lower() == "rain":
            skipped.append((field, "Rain expected"))
            continue

        # Schedule if enough water is available
        if field["water_required"] <= remaining_water:
            field["slot"] = slot

            scheduled.append(field)

            remaining_water -= field["water_required"]
            slot += 1

        else:
            skipped.append((field, "Insufficient water"))

    return scheduled, skipped, remaining_water


def display_results(scheduled, skipped, available_water, remaining_water):

    print("\n" + "=" * 65)
    print("       SMART AGRICULTURE IRRIGATION OPTIMIZER")
    print("=" * 65)

    print(f"\nAvailable Water : {available_water} L")

    print("\nOPTIMIZED IRRIGATION SCHEDULE")
    print("-" * 65)

    if scheduled:
        print(
            f"{'Slot':<6}"
            f"{'Field':<12}"
            f"{'Moisture':<12}"
            f"{'Water(L)':<12}"
            f"{'Priority':<12}"
        )

        print("-" * 65)

        for field in scheduled:
            print(
                f"{field['slot']:<6}"
                f"{field['name']:<12}"
                f"{str(field['soil_moisture']) + '%':<12}"
                f"{field['water_required']:<12}"
                f"{field['priority_score']:<12}"
            )
    else:
        print("No fields could be scheduled.")

    total_used = available_water - remaining_water

    print("\n" + "-" * 65)
    print(f"Total Water Used      : {total_used} L")
    print(f"Remaining Water       : {remaining_water} L")
    print(f"Fields Scheduled      : {len(scheduled)}")
    print(f"Fields Not Scheduled  : {len(skipped)}")

    # Water utilization
    utilization = (total_used / available_water) * 100

    print(f"Water Utilization     : {utilization:.2f}%")

    print("-" * 65)

    if skipped:
        print("\nSKIPPED FIELDS")
        print("-" * 65)

        for field, reason in skipped:
            print(
                f"{field['name']:<12} "
                f"Priority: {field['priority_score']:<6} "
                f"Reason: {reason}"
            )

    print("\n" + "=" * 65)


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------

fields = [
    {
        "name": "Field A",
        "soil_moisture": 25,
        "water_required": 40,
        "crop_priority": 5,
        "deadline": 2,
        "weather": "Sunny"
    },
    {
        "name": "Field B",
        "soil_moisture": 45,
        "water_required": 30,
        "crop_priority": 3,
        "deadline": 3,
        "weather": "Rain"
    },
    {
        "name": "Field C",
        "soil_moisture": 20,
        "water_required": 50,
        "crop_priority": 5,
        "deadline": 1,
        "weather": "Sunny"
    },
    {
        "name": "Field D",
        "soil_moisture": 35,
        "water_required": 25,
        "crop_priority": 4,
        "deadline": 2,
        "weather": "Cloudy"
    },
    {
        "name": "Field E",
        "soil_moisture": 50,
        "water_required": 20,
        "crop_priority": 2,
        "deadline": 4,
        "weather": "Sunny"
    }
]

available_water = 120

scheduled, skipped, remaining_water = greedy_irrigation_schedule(
    fields,
    available_water
)

display_results(
    scheduled,
    skipped,
    available_water,
    remaining_water
)
