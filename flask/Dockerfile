FROM andrezyk/alpine_py3_r_deps:latest

COPY . proj

WORKDIR /proj/flask_r_interpolaton/

RUN pip3 install -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org

EXPOSE 8080:8080

CMD ["python3", "run_prod.py"]
