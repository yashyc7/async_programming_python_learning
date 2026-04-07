# Async Python Learning Plan

## Goal

Master async programming in Python with production-level understanding:

* Concurrency mindset (not just syntax)
* Event loop internals
* Scalable async patterns
* Real-world backend usage

---

## Chapter 1 — Why Async Exists (Mental Model)

### Concepts

* Blocking vs Non-blocking
* Sync vs Async execution
* CPU-bound vs I/O-bound
* Concurrency vs Parallelism

### Example

Simulate 3 API calls using `time.sleep()` (sync) vs `asyncio.sleep()` (async) and compare execution time.

### Exercise

Write a script that:

* Makes 5 fake API calls (use sleep)
* First runs them synchronously
* Then runs them asynchronously
* Print total execution time for both

---

## Chapter 2 — Coroutines & async/await

### Concepts

* `async def`
* Coroutine objects
* `await` mechanics
* Awaitables

### Example

Create an async function that fetches user data (simulated delay) and prints it.

### Exercise

* Create 3 async functions:

  * fetch_user()
  * fetch_orders()
  * fetch_payments()
* Chain them using `await`
* Ensure execution order is correct

---

## Chapter 3 — Event Loop (asyncio)

### Concepts

* Event loop lifecycle
* `asyncio.run()`
* Task scheduling
* Execution flow

### Example

Manually create and run tasks using the event loop.

### Exercise

* Create 3 coroutines with different delays
* Observe execution order
* Log timestamps to understand scheduling

---

## Chapter 4 — Tasks & Concurrency

### Concepts

* `asyncio.create_task()`
* `asyncio.gather()`
* Concurrent execution
* Fire-and-forget vs controlled execution

### Example

Run multiple API calls concurrently using `gather`

### Exercise

* Run 10 async tasks concurrently
* Each task should:

  * Sleep random time
  * Return result
* Collect all results and print

---

## Chapter 5 — Async I/O (Real Power)

### Concepts

* Async HTTP requests (`aiohttp`)
* Async file handling
* Intro to async DB

### Example

Fetch data from multiple APIs concurrently

### Exercise

* Call 5 public APIs concurrently
* Parse JSON responses
* Aggregate results into one output

---

## Chapter 6 — Error Handling & Cancellation

### Concepts

* Exception handling in async
* Task cancellation
* Timeouts (`asyncio.wait_for`)

### Example

Handle failure in one async task without crashing others

### Exercise

* Create 5 tasks
* Force 1 to fail
* Handle errors gracefully
* Add timeout logic

---

## Chapter 7 — Async Patterns (Advanced)

### Concepts

* Producer–Consumer
* Fan-out / Fan-in
* Rate limiting
* Backpressure

### Example

Implement producer-consumer using `asyncio.Queue`

### Exercise

* Create:

  * Producer (adds tasks)
  * Multiple consumers (process tasks)
* Limit queue size
* Handle overload safely

---

## Chapter 8 — Performance & Pitfalls

### Concepts

* When NOT to use async
* GIL limitations
* Blocking calls inside async
* Debugging async code

### Example

Show how blocking code breaks async performance

### Exercise

* Insert blocking call inside async flow
* Measure performance impact
* Fix it properly

---

## Chapter 9 — Async in Frameworks

### Concepts

* FastAPI async routes
* Async DB drivers
* Background tasks

### Example

Create async FastAPI endpoint calling external APIs

### Exercise

* Build API:

  * Endpoint calls 3 async services
  * Aggregates response
* Add timeout + error handling

---

## Chapter 10 — Mini Project (Production Thinking)

### Project

Async API Aggregator System

### Features

* Concurrent requests (100+)
* Rate limiting
* Retry logic
* Logging
* Error handling

### Exercise

Build system with:

* Configurable concurrency
* Retry on failure
* Timeout handling
* Structured logging

---

## Rules While Learning

* Run every example
* Break code intentionally
* Measure performance
* Think in "tasks", not "functions"
* Never block inside async code

---