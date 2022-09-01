
#Just getting the actual time.
import datetime
from turtle import title
e = datetime.datetime.now()
#Asking user's name, and printing name + date + time and remove WS and Capt.
name = input("Whats ur name pal? ").title().strip()
print ("Hi " + name + ", how was your day?" + ". ", end="")
print ("Today's date and time is: %s/%s/%s." % (e.day, e.month, e.year)," %s:%s:%s" % (e.hour, e.minute, e.second))




[33mcommit 71181482982994af029466b6691bd7f13aab2891[m[33m ([m[1;36mHEAD -> [m[1;32mmaster[m[33m)[m
Author: nico <nicomarruccelli@live.com>
Date:   Wed Aug 31 22:12:14 2022 -0300

    alltogheterwellformed

[33mcommit d4ef3c68fa8f9b72979e4729307df1ec749bbc43[m
Author: nico <nicomarruccelli@live.com>
Date:   Wed Aug 31 20:09:44 2022 -0300

    with time working

[33mcommit 26b7ab0eb3f9b96cc38cf047c870bbdc81023c3f[m[33m ([m[1;31morigin/master[m[33m)[m
Merge: 624053b ba839e7
Author: nico <nicomarruccelli@live.com>
Date:   Tue Aug 30 23:02:32 2022 -0300

    Merge branch 'master' of https://github.com/Menack/first-git

[33mcommit 624053bbf8bee77a05de121b42bd4b9d2d96fdd0[m
Author: nico <nicomarruccelli@live.com>
Date:   Tue Aug 30 22:47:22 2022 -0300

    now with py

[33mcommit 67d6e7f4f7c43ae0bb7619b749dd85bf9893cd0e[m
Author: nico <nicomarruccelli@live.com>
Date:   Tue Aug 30 22:18:02 2022 -0300

    now with py

[33mcommit ba839e7dd1566ba01ffdb208d7bb79e0d30c9a26[m
Author: Nicolas Marruccelli <110432313+Menack@users.noreply.github.com>
Date:   Tue Aug 30 20:38:49 2022 -0300

    Create README.md

[33mcommit 52cb862e324f4985a5903ca30d65edade65d145e[m
Author: nico <nicomarruccelli@live.com>
Date:   Tue Aug 30 19:33:52 2022 -0300

    firstTest
