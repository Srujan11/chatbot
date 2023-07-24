#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import wikipedia

def recognize_celebrities(photo):
    celebrityInfo = []
    session = boto3.Session(profile_name='default')
    client = session.client('rekognition')

    with open(photo, 'rb') as image:
        response = client.recognize_celebrities(Image={'Bytes': image.read()})

    print('Detected faces for ' + photo)
    for celebrity in response['CelebrityFaces']:
        print('Name: ' + celebrity['Name'])
        print('Id: ' + celebrity['Id'])
        print('KnownGender: ' + celebrity['KnownGender']['Type'])
        print('Smile: ' + str(celebrity['Face']['Smile']['Value']))
        print('Position:')
        print('   Left: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Height']))
        print('   Top: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Top']))
        print('Info')
        for url in celebrity['Urls']:
            print('   ' + url)
        print()

        celebrity_data = {}
        celebrity_data["name"] = celebrity['Name']
        wiki_data = wikipedia.summary(celebrity_data["name"], sentences = 2)
        celebrity_data["description"] = wiki_data
        celebrityInfo.append(celebrity_data)
    return celebrityInfo

# def main():
#     photo = ''
#     celeb_count = recognize_celebrities(photo)
#     print("Celebrities detected: " + str(celeb_count))

# if __name__ == "__main__":
#     main()