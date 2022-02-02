RUN git clone https://github.com/AOSOFJ/UB-BACK.git /root/userbot

WORKDIR /root/userbot

RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3", "-m", "userlbot"]
