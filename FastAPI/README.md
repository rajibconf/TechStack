# FastAPI
## __Usage:__
>
> _Please make sure `python-3.10` or plus is installed in the system._
>
> _NOTE for Windows users: Please use `Powershell or Git Bash` for the following steps_

1. ### Prepare project directory
    - Create a virtual environment using `python`. (Test via `python -V`. Must be python 3.10 or plus)
    - `Activate` the virtual environment. (Windows: `.\venv\Scripts\activate`)
    ```shell script
    cd FastAPI
    python -m venv venv
    source venv/bin/activate
    # Windows: .\venv\Scripts\activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    # Run the live server with uvicorn:
    uvicorn main:app --reload
    ```
### Check it
> Open your browser at http://127.0.0.1:8000.
### Interactive API docs with Swagger UI
>Now go to http://127.0.0.1:8000/docs
### Alternative API docs
> And now, go to http://127.0.0.1:8000/redoc
