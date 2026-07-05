# TASK 1: Project Structure
#
# ROUTER LAYER (Handler Layer)
#
# Responsibilities:
# - Receive HTTP requests
# - Validate input using Pydantic models
# - Call service layer
# - Return HTTP responses
#
# What NOT to do here:
# - Business logic
# - Direct data access
# - Email sending
# - File operations
#
# This layer only knows about HTTP and how to talk to services.
