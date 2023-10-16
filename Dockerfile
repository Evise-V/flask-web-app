FROM python:3.12-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt 

COPY ./website /code/website

COPY ./main.py /code/main.py
 
RUN set -ex \
    # Create a non-root user
    && useradd -m appuser \
    # && addgroup --system --gid 1001 appgroup \
    # && adduser --system --uid 1001 --gid 1001 --no-create-home appuser \
    # Upgrade the package index and install security upgrades
    && apt-get update \
    && apt-get upgrade -y \
    # Install dependencies
    # && pip install -r requirements.txt \
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

USER appuser

EXPOSE 8000

ENTRYPOINT ["flask", "--app=main", "run"]
CMD ["--host=0.0.0.0", "--port=8000"]
