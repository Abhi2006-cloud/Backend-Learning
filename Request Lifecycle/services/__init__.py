# TASK 1: Project Structure
#
# SERVICE LAYER (Business Logic Layer)
#
# Responsibilities:
# - Implement business rules
# - Data processing and transformation
# - Coordinate between repositories
# - Orchestrate business operations
#
# What NOT to do here:
# - HTTP-specific logic
# - Direct database queries (use repositories)
# - Input validation (that's handler's job)
#
# This layer contains the "brains" of the application.
# It knows WHAT to do, not HOW to receive requests or store data.
