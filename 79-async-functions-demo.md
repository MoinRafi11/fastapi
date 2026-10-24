
# 79 - Async Functions Demo in Python

## 1. Introduction

Asynchronous programming allows a program to perform other tasks while waiting for operations such as network requests, database queries, or file operations to complete.

Python supports asynchronous programming through `async` and `await`.

These features are especially useful when building APIs, backend services, and applications that handle multiple I/O operations.

In this guide, we will learn:

- What asynchronous programming is.
- The difference between synchronous and asynchronous functions.
- How `async` and `await` work.
- How to run asynchronous functions.
- How to execute multiple tasks concurrently.
- How asynchronous functions are used in FastAPI.

## 2. What Is a Synchronous Function?

A synchronous function executes its operations in sequence. When one operation blocks while waiting for a result, the following operations in that execution flow must wait.

### Example

```python
import time


def task_one():
    print("Task 1 started")
    time.sleep(2)
    print("Task 1 completed")


def task_two():
    print("Task 2 started")
    time.sleep(1)
    print("Task 2 completed")


task_one()
task_two()
```

### Output

```text
Task 1 started
Task 1 completed
Task 2 started
Task 2 completed
```

### Explanation

- `task_one()` takes approximately two seconds to complete.
- `task_two()` starts only after `task_one()` finishes.
- The total execution time is approximately three seconds.

The `time.sleep()` function blocks the current thread while it waits.

## 3. What Is an Asynchronous Function?

An asynchronous function is defined using the `async def` syntax.

It can suspend its execution at an `await` expression, allowing an asynchronous event loop to run other tasks while the current task waits for an operation to complete.

### Example

```python
import asyncio


async def greet():
    print("Hello")
    await asyncio.sleep(2)
    print("Welcome to asynchronous programming")


asyncio.run(greet())
```

### Output

```text
Hello
Welcome to asynchronous programming
```

### Explanation

- `async def greet()` defines a coroutine function.
- Calling `greet()` creates a coroutine object; it does not execute the function to completion by itself.
- `await asyncio.sleep(2)` suspends the coroutine without blocking the event loop.
- `asyncio.run(greet())` runs the coroutine using an event loop.

**Important:** `asyncio.sleep()` is asynchronous, whereas `time.sleep()` blocks the thread.

## 4. Understanding `async` and `await`

### The `async` Keyword

The `async` keyword is used to define a coroutine function.

```python
async def my_function():
    print("This is an asynchronous function")
```

Calling the function creates a coroutine object that must be awaited or scheduled to execute.

### The `await` Keyword

The `await` keyword waits for an awaitable operation to produce its result while allowing the event loop to run other tasks.

```python
import asyncio


async def fetch_data():
    await asyncio.sleep(1)
    return "Data received"


async def main():
    result = await fetch_data()
    print(result)


asyncio.run(main())
```

### Output

```text
Data received
```

Here, `main()` awaits `fetch_data()`, allowing the coroutine to complete before printing the result.

## 5. Running Multiple Tasks Concurrently

One of the main advantages of asynchronous programming is that multiple I/O-bound tasks can make progress concurrently.

Consider two operations that each wait for two seconds.

### Example Using Sequential Execution

```python
import asyncio


async def task_one():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 completed")


async def task_two():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 completed")


async def main():
    await task_one()
    await task_two()


asyncio.run(main())
```

### Expected Output

```text
Task 1 started
Task 1 completed
Task 2 started
Task 2 completed
```

The total execution time is approximately four seconds because the tasks are awaited sequentially.

### Example Using `asyncio.gather()`

```python
import asyncio


async def task_one():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 completed")


async def task_two():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 completed")


async def main():
    await asyncio.gather(
        task_one(),
        task_two()
    )


asyncio.run(main())
```

### Expected Output

```text
Task 1 started
Task 2 started
Task 1 completed
Task 2 completed
```

The total execution time is approximately two seconds because both tasks wait concurrently.

The exact output timing can vary depending on the environment.

### Key Difference

| Sequential Execution | Concurrent Execution |
|---|---|
| Tasks are awaited one after another. | Tasks can make progress during each other's waits. |
| Two two-second waits take about four seconds. | Two two-second waits take about two seconds. |
| Uses sequential `await` expressions. | Can use `asyncio.gather()`. |

Asynchronous concurrency is especially beneficial for I/O-bound operations. It does not automatically speed up CPU-intensive calculations.

## 6. Using `asyncio.create_task()`

The `asyncio.create_task()` function schedules a coroutine to run as a task on the current event loop.

This allows the task to make progress while the program performs other asynchronous operations.

### Example

```python
import asyncio


async def download_file():
    print("Downloading file...")
    await asyncio.sleep(3)
    print("Download completed")


async def main():
    task = asyncio.create_task(download_file())

    print("Doing other work...")

    await asyncio.sleep(1)

    print("Other work completed")

    await task


asyncio.run(main())
```

### Expected Output

```text
Downloading file...
Doing other work...
Other work completed
Download completed
```

### Explanation

- `asyncio.create_task()` schedules `download_file()`.
- The program continues with other operations.
- The download coroutine progresses while the program waits.
- `await task` ensures the task completes before `main()` finishes.

Always consider how tasks are completed and how exceptions are handled, especially when working with multiple concurrent tasks.

## 7. Async Functions with Return Values

Asynchronous functions can return values just like regular Python functions.

### Example

```python
import asyncio


async def calculate_total():
    await asyncio.sleep(1)
    return 100 + 200


async def main():
    total = await calculate_total()
    print(f"Total: {total}")


asyncio.run(main())
```

### Output

```text
Total: 300
```

The `return` statement provides the result, and `await` retrieves that result when the coroutine completes.

## 8. Async Functions with Parameters

Asynchronous functions can accept parameters and use them in their operations.

### Example

```python
import asyncio


async def greet_user(name):
    await asyncio.sleep(1)
    return f"Hello, {name}!"


async def main():
    message = await greet_user("Moin")
    print(message)


asyncio.run(main())
```

### Output

```text
Hello, Moin!
```

The function accepts a name, waits asynchronously, and returns a greeting.

## 9. Using `async` Functions in FastAPI

FastAPI supports both synchronous (`def`) and asynchronous (`async def`) endpoint functions.

An asynchronous endpoint is useful when it calls libraries that support asynchronous operations, such as an asynchronous HTTP client or database driver.

### Example

```python
from fastapi import FastAPI
import asyncio

app = FastAPI()


@app.get("/")
async def home():
    await asyncio.sleep(1)
    return {"message": "Hello from FastAPI"}
```

### Explanation

- `@app.get("/")` registers a GET endpoint.
- `async def home()` defines an asynchronous endpoint.
- `await asyncio.sleep(1)` simulates a non-blocking wait.
- The endpoint returns a JSON response after the wait.

Run the application using:

```bash
uvicorn main:app --reload
```

Open the following URL:

```text
http://127.0.0.1:8000/
```

Expected response:

```json
{
  "message": "Hello from FastAPI"
}
```

The sleep is included only to demonstrate asynchronous behavior. A real application would typically await an actual I/O operation.

## 10. Async vs Sync in FastAPI

| Feature | Synchronous Endpoint | Asynchronous Endpoint |
|---|---|---|
| Definition | `def` | `async def` |
| Typical use | Synchronous operations | Asynchronous I/O operations |
| Can use `await` directly | No | Yes |
| Blocking I/O | Can block its worker thread | Can block the event loop if called directly |
| Best suited for | Ordinary synchronous libraries | Libraries supporting async operations |

FastAPI handles normal synchronous path operation functions in a thread pool. Asynchronous endpoints run on the event loop, so blocking operations should be avoided inside them.

**Important:** Do not change every function to `async def` automatically. Choose the function type based on the libraries and operations being used.

## 11. Common Mistakes

### Mistake 1: Calling a Coroutine Without Awaiting It

Incorrect:

```python
import asyncio


async def greet():
    print("Hello")


async def main():
    greet()


asyncio.run(main())
```

The call to `greet()` creates a coroutine object but does not execute it to completion. Python may issue a warning that the coroutine was never awaited.

Correct:

```python
import asyncio


async def greet():
    print("Hello")


async def main():
    await greet()


asyncio.run(main())
```

### Mistake 2: Using `time.sleep()` Inside an Async Function

Incorrect for non-blocking asynchronous code:

```python
import asyncio
import time


async def task():
    time.sleep(2)
    print("Task completed")


asyncio.run(task())
```

`time.sleep(2)` blocks the thread, preventing the event loop from running other tasks during the wait.

Correct:

```python
import asyncio


async def task():
    await asyncio.sleep(2)
    print("Task completed")


asyncio.run(task())
```

### Mistake 3: Forgetting to Await a Result

Incorrect:

```python
async def get_data():
    return "Data"


async def main():
    result = get_data()
    print(result)
```

This prints a coroutine object rather than the returned string.

Correct:

```python
async def get_data():
    return "Data"


async def main():
    result = await get_data()
    print(result)
```

## 12. When Should You Use Async Programming?

Asynchronous programming is especially useful when an application spends significant time waiting for external operations.

Common examples include:

- Making HTTP requests to external APIs.
- Handling multiple network connections.
- Querying databases through asynchronous drivers.
- Building real-time applications.
- Managing many concurrent I/O-bound operations.
- Developing API endpoints that call multiple services.

For CPU-intensive work, such as large mathematical calculations or image processing, asynchronous programming alone does not provide parallel CPU execution. Multiprocessing, worker processes, or other suitable approaches may be more appropriate.

## 13. Best Practices

- Use `async def` for coroutine functions.
- Use `await` when calling awaitable operations.
- Prefer asynchronous libraries when building an asynchronous workflow.
- Avoid blocking operations on the event loop.
- Use `asyncio.gather()` or tasks when independent operations can run concurrently.
- Ensure background tasks are completed or managed appropriately.
- Handle exceptions from concurrent tasks.
- Use `asyncio.run()` to run a top-level coroutine in a normal standalone Python script.
- Avoid calling `asyncio.run()` inside an already running event loop.

## 14. Summary

Asynchronous programming helps Python applications handle waiting efficiently.

Key concepts covered in this guide:

- `async def` defines a coroutine function.
- `await` suspends a coroutine until an awaitable operation completes.
- `asyncio.run()` executes a top-level coroutine.
- `asyncio.gather()` allows multiple awaitables to make progress concurrently.
- `asyncio.create_task()` schedules a coroutine as a task.
- `asyncio.sleep()` provides a non-blocking delay.
- FastAPI supports asynchronous endpoints.
- Async programming is particularly useful for I/O-bound workloads.

Understanding these concepts helps developers build responsive APIs and services that can handle concurrent operations efficiently.
