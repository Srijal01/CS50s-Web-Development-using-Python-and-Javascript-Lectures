 # Lecture 8 — Scalability and Security

## Table of contents
- Introduction
- Scalability
- Scaling
- Load Balancing
- Autoscaling
	- Server Failure
- Scaling Databases
	- Database Replication
- Caching
- Security
	- Git and GitHub
	- HTML
	- HTTPS
		- Secret-Key Cryptography
		- Public-Key Cryptography
	- Databases
		- APIs
		- Environment Variables
	- JavaScript
		- Cross-Site Request Forgery (CSRF)
		- Cross-Site Scripting (XSS)
- What's next


## Introduction
This lecture covers how to scale web applications so they can serve many users, and how to secure web apps against common threats. Topics include servers and hosting options, load balancing, autoscaling, database scaling and replication, caching, and web security best practices.


## Scalability
Hosting choices:
- On-premise: full control and customization, higher startup cost and maintenance overhead.
- Cloud hosting: easier to manage and scale, costs based on usage, less hardware maintenance.

Benchmarking tools (e.g., Apache Bench) help determine how many requests a single server can handle before crashing.


## Scaling
- Vertical scaling: upgrade a single server (limited by hardware ceiling).
- Horizontal scaling: add more servers and distribute load across them.


## Load Balancing
Load balancers distribute incoming requests among multiple servers. Common strategies:
- Random
- Round-robin
- Fewest connections

Session handling strategies when using multiple servers:
- Sticky sessions: route the same user to the same server (can overload servers).
- Database-backed sessions: store sessions in a central DB accessible to all servers (additional latency).
- Client-side sessions (cookies): avoid server-side storage but raise security and size concerns.

Images:
- Server request diagram: https://cs50.harvard.edu/web/notes/8/images/server0.png


## Autoscaling
- Autoscaling adjusts the number of running servers based on load. Useful for traffic spikes (e.g., seasonal traffic), but provisioning takes time and more servers increase failure surface.
- To mitigate single points of failure, use multiple load balancers and heartbeat checks.


## Scaling Databases
Strategies:
- Vertical partitioning: split data into multiple tables (schema redesign).
- Horizontal partitioning (sharding): split a table into multiple tables with the same schema but different rows.

### Database Replication
- Single-primary (primary/replica): one writable primary; others are read-only replicas. Easier to keep consistent but still a write single point of failure.
- Multi-primary (multi-master): all replicas accept writes — helps availability but introduces update/uniqueness/delete conflicts and complexity.

Diagrams (CS50):
- Single-primary: https://cs50.harvard.edu/web/notes/8/images/single_primary.png
- Multi-primary: https://cs50.harvard.edu/web/notes/8/images/multi_primary.png


## Caching
Reduce expensive database and template rendering calls by caching:
- Client-side caching via HTTP headers, e.g.:

```
Cache-Control: max-age=86400
```

- ETag: version identifier for conditional requests.
- Server-side caching: shared cache layer accessible to all servers (e.g., Redis, Memcached). Django provides a cache framework with:
	- Per-view caching
	- Template-fragment caching
	- Low-level cache API

Image: https://cs50.harvard.edu/web/notes/8/images/server_cache.png


## Security
Security spans many layers: source control, HTML, transport (HTTPS), databases, APIs, and client-side code.

### Git and GitHub
- Never commit secrets (passwords, API keys) to version control. Use environment variables or secret managers instead.

### HTML
- Phishing: attackers can serve pages that mimic legitimate sites and send credentials to attackers.
- Be careful when rendering user-provided HTML or links.

Example of a deceptive link HTML:

```
<a href="https://cs50.harvard.edu/web/">https://www.google.com/</a>
```

Image (phishing): https://cs50.harvard.edu/web/notes/8/images/phishing.gif


### HTTPS
Transport security relies on cryptography:
- Secret-key (symmetric) cryptography: fast and secure but requires a pre-shared key.
- Public-key (asymmetric) cryptography: uses a public/private key pair (enables HTTPS).

HTTPS ensures encrypting traffic between client and server, protecting data in transit.

Images: server transfer diagram https://cs50.harvard.edu/web/notes/8/images/servers.png


### Databases
- Never store plaintext passwords. Store password hashes (one-way). Django handles hashing for you.

Bad table (plaintext passwords): https://cs50.harvard.edu/web/notes/8/images/passwords.png
Good table (hashed passwords): https://cs50.harvard.edu/web/notes/8/images/hashes.png

When designing flows (e.g., forgotten-password pages), consider information leakage (e.g., revealing whether an email is registered) and timing attacks.

#### APIs
- Use API keys, rate-limiting, and route authentication to protect endpoints and mitigate DoS attacks.

#### Environment Variables
- Keep secrets out of source code by reading them from environment variables on the server.


## JavaScript
### Cross-Site Request Forgery (CSRF)
- CSRF tricks a user's browser into submitting state-changing requests (GET or POST) to a site where the user is authenticated.
- Mitigation: use CSRF tokens (Django provides built-in protection) and require POST for state changes.

Example attack (auto-submitting form):

```
<body onload="document.forms[0].submit()">
	<form action="https://yourbank.com/transfer" method="post">
		<input type="hidden" name="to" value="brian">
		<input type="hidden" name="amt" value="2800">
	</form>
</body>
```

### Cross-Site Scripting (XSS)
- XSS occurs when an attacker injects JavaScript into pages viewed by other users (e.g., reflected or stored XSS).
- Always sanitize or escape user input when rendering it in pages. Prefer framework-provided escaping (Django templates auto-escape by default).

Example vulnerable view:

```
def index(request, path):
		return HttpResponse(f"Requested Path: {path}")
```

This could allow a user to craft a URL that injects script into the response.


## What’s next?
Further technologies and frameworks to explore:
- Server-side: Express.js, Ruby on Rails, Flask, ...
- Client-side: Angular, React, Vue, React Native, ...

Deployment platforms:
- AWS, GitHub Pages, Heroku, Netlify, Google Cloud, Microsoft Azure, ...


## References / Resources
- CS50 Web course notes: https://cs50.harvard.edu/web/notes/8/
- Django cache docs: https://docs.djangoproject.com/en/4.0/topics/cache/


---
Updated based on CS50 Lecture 8 notes.
