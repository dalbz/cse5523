artists = [line.split('#')[1].strip() for line in open('data/svmlight/svmlight_test.txt')]
values = [float(line.strip()) for line in open('data/svmlight/output.txt')]

results_file = open('data/svmlight/predicted_artists.txt', 'w')

for i in range(0, len(artists)) :
    if (values[i] > 0):
        results_file.write(artists[i] + '\n\t\t' + str(values[i]) + '\n')
