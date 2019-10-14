from bisection_implementation import (analyze_func, bisection_iter,
                                      random_email_list)

domain_list = ["yaexample.com", "goexample.com", "example.com"]

# Generate email list and record timing
emails, email_time = analyze_func(random_email_list, 10, domain_list, 1000000)

# Add target email and sort list
target = "mashrur@example.com"
emails.append(target)
sorted_emails = sorted(emails)

# Search for target and record timing
(index, found), search_time = analyze_func(bisection_iter, target, sorted_emails)

# Print results
print(found)
if index:
    print(f"Element at {index} is {sorted_emails[index]}")
print(email_time)
print(search_time)
