from DataFormatter import DataFormatter
import pickle
import pandas as pd
import sys

# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', -1)

if __name__ == '__main__':
    rally_urls = []
    rally_url_file = open('trump_rally_urls.txt')
    for line in rally_url_file:
        rally_urls.append(line.replace('\n', ''))
    rally_url_file.close()

    # rally_location = ['Charlotte_NC', 'Charleston_SC', 'Las_Vegas_NV', 'Colorado_Springs_CO', 'Phoenix_AZ',
                      # 'Manchester_NH_01', 'Des_Moines, IA', 'Wildwood_NJ', 'Milwaukee_WS', 'Battle_Cree_MI',
                      # 'Hershey_PA', 'Lexington_KY', 'Tupelo_MS', 'Dallas_TX', 'Minneapolis_MN', 'Houston_TX',
                      # 'Albuquerque_NM', 'Fayetteville_NC', 'Manchester_NH_02', 'Cincinnati_OH', 'Greenville_NC']

    try:
        pickle_in = open('rally_df.pickle', 'rb')
        rally_df = pickle.load(pickle_in)
        pickle_in.close()
    except:
        rally_transcripts = []
        print("Loading and Cleaning URLs...")
        for url in rally_urls:
            transcript = DataFormatter.rally_url_to_transcript(url)
            clean_transcript = DataFormatter.clean_transcript(transcript)
            rally_transcripts.append(clean_transcript)

        rally_df = pd.DataFrame(rally_transcripts)
        rally_df.columns = ['transcript']
        rally_df['type'] = 'rally'

        print("Saving DataFrame...")
        DataFormatter.pickle_object(rally_df, 'rally_df.pickle')

        print("Done.")
        sys.exit()

    print(rally_df.head())
