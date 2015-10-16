# Comments before FROM
FROM ubuntu

RUN apt-get update && apt-get install -y python

# Comments below a RUN
#Comment without a leading space

CMD bash
