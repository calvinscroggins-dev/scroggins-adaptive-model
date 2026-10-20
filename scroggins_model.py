
"""
CSC505 - Principles of Software Engineering
Scroggins Adaptive Model (SAM)

This program collects user-defined phase names and descriptions,
then displays the adaptive software development lifecycle.
"""

def main():
    print("=" * 65)
    print("SCROGGINS ADAPTIVE MODEL (SAM)")
    print("An Adaptive Software Engineering Lifecycle")
    print("=" * 65)

    default_phases = [
        ("Discovery & Communication",
         "Gather stakeholder requirements and define business objectives."),
        ("Adaptive Planning",
         "Estimate effort, assess risks, and schedule development sprints."),
        ("Iterative Modeling",
         "Analyze requirements, design solutions, and review with stakeholders."),
        ("Continuous Construction & Testing",
         "Develop code, automate testing, and perform peer validation."),
        ("Incremental Deployment",
         "Release validated features, obtain user acceptance, and provide support."),
        ("Monitoring & Continuous Improvement",
         "Monitor performance, collect feedback, and prioritize changes.")
    ]

    phases = []

    print("\nEnter a name and description for each phase.")
    print("Press Enter to accept the suggested value.\n")

    for number, (default_name, default_description) in enumerate(
        default_phases, start=1
    ):
        print(f"\n--- Phase {number} ---")

        name = input(f"Phase name [{default_name}]: ").strip()
        if not name:
            name = default_name

        description = input(
            f"Description [{default_description}]: "
        ).strip()
        if not description:
            description = default_description

        phases.append((name, description))

    print("\n" + "=" * 65)
    print("SCROGGINS ADAPTIVE MODEL - PHASE SUMMARY")
    print("=" * 65)

    for number, (name, description) in enumerate(phases, start=1):
        print(f"\nPhase {number}: {name}")
        print(f"  Description: {description}")

    print("\n" + "-" * 65)
    print("MODEL STRUCTURE")
    print("-" * 65)

    for number, (name, _) in enumerate(phases, start=1):
        print(f"{number}. {name}")
        if number < len(phases):
            print("   |")
            print("   v")

    print("\nTESTING DECISION")
    print("Testing Passed?")
    print("  Yes -> Proceed to Incremental Deployment")
    print("  No  -> Return to Continuous Construction & Testing")

    print("\nADAPTIVE FEEDBACK LOOPS")
    print("1. Iterative Modeling -> Adaptive Planning")
    print("   Requirements Refinement")
    print("2. Continuous Construction & Testing -> Iterative Modeling")
    print("   Test Feedback")
    print("3. Monitoring & Continuous Improvement -> Discovery & Communication")
    print("   Continuous Improvement")

    print("\n" + "=" * 65)
    print("SAM supports iterative development, continuous testing,")
    print("stakeholder collaboration, and ongoing improvement.")
    print("=" * 65)


if __name__ == "__main__":
    main()
