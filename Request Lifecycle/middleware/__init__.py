# TASK 1: Project Structure
#
# MIDDLEWARE LAYER (Cross-Cutting Concerns)
#
# Responsibilities:
# - Logging
# - Authentication
# - Rate limiting
# - Request ID generation
# - Error handling
# - Any concern that applies to ALL requests
#
# What NOT to do here:
# - Business logic
# - Route-specific logic
# - Data access
#
# Middleware runs before and after every request.
# It's the perfect place for cross-cutting concerns.
