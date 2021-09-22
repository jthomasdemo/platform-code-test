#!/usr/bin/python3
def update_quality(awards):
    for award in awards:
        if award.name != 'Blue First' and award.name != 'Blue Compare' and award.name != 'Blue Star':
            if award.quality > 0:
                if award.name != 'Blue Distinction Plus':
                    award.quality -= 1
                elif award.name == 'Blue Star':
                    if award.expires_in < 25 and award.quality < 50:
                        award.quality += 1
                    if award.expires_in < 20 and award.quality < 50:
                        award.quality += 0.9
                    if award.expires_in < 15:
                        if award.quality < 50:
                            award.quality += 0.7
                    if award.expires_in < 11:
                        if award.quality < 50:
                            award.quality += 0.5
                    if award.expires_in < 6:
                        if award.quality < 50:
                            award.quality += 0.3
                    if award.expires_in < 3:
                        if award.quality < 50:
                            award.quality += 0.2
                    if award.expires_in < 1:
                        if award.quality < 50:
                            award.quality += 0.1
        else:
            if award.quality < 50:
                award.quality += 1
                if award.name == 'Blue Compare':
                    if award.expires_in < 11:
                        if award.quality < 50:
                            award.quality += 1
                    if award.expires_in < 6:
                        if award.quality < 50:
                            award.quality += 1

        if award.name != 'Blue Distinction Plus':
            award.expires_in -= 1

        if award.expires_in < 0:
            if award.name == 'Blue Star':
                if award.quality > 0:
                    award.quality -= 2

            elif award.name != 'Blue First':
                if award.name != 'Blue Compare':
                    if award.quality > 0:
                        if award.name != 'Blue Distinction Plus':
                            award.quality -= 1
                elif award.name == 'Blue Star':
                    if award.quality > 0:
                        award.quality -= 2
                else:
                    award.quality = award.quality - award.quality
