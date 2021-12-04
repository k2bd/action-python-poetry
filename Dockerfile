FROM python:3.9

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

RUN pip install "poetry==1.1.11"

COPY poetry.lock pyproject.toml ./
RUN poetry install --no-dev

COPY . .
RUN poetry build && pip install dist/*.whl

CMD ["python", "-m", "action_python_poetry"]
