FROM jupyter/base-notebook:python-3.8.8 
COPY requirements.txt /home/jovyan
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5006 
# default port for bokeh

ENTRYPOINT ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root"]