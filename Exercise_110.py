movie_ratings = input('what is the rating of the movie? ')

if movie_ratings == 'universal':
    print('everyone can watch')
elif movie_ratings == 'pg':
    print('General viewing, but some scenes may be unsuitable for young children ')
elif movie_ratings == '12':
    print('Films classified 12A and video works classified 12 contain material that is not generally suitable for '
          'children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an '
          'adult.')
elif movie_ratings == '15':
    print('No one younger than 15 may see a 15 film in a cinema.')
elif movie_ratings == '18':
    print("No one younger than 18 may see an 18 film in a cinema")
