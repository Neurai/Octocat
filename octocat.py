user_art = ["", "    ", "    ", "    "] #Key [Left eye, Right eye, Nose, Mouth]

def printer(counter):
                                        #art is generated from an image then modified, @ http://www.text-image.com
                                            #its the Github logo, Octocat!:D
    octocat_image =    """
                     `:+syhdmNNNmdhys+:`
                 `:sdNNNNNNNNNNNNNNNNNNNds:`
               -smNNNNNNNNNNNNNNNNNNNNNNNNNms-
             :hNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNh:
           .sNNNNNy+oydmNN-Octocat-NNmdyo+yNNNNNy.
          -dNNNNNN.   `-++"::---::"++-`   .NNNNNNd-
         -mNNNNNNN.                       .NNNNNNNm-
        `dNNNNNNNd.                       .dNNNNNNNd`
        +NNNNNNNh`                         `hNNNNNNN+
        hNNNNNNNx    1{}      1{}     :NNNNNNNh
        NNNNNNNN.                           .NNNNNNNN
        mNNNNNNNk         1 {}           -NNNNNNNm
        yNNNNNNNh`                         `hNNNNNNNy
        :NNNNNNNNh-       1 {}         -hNNNNNNNN:
         sNNNNmmNNms:.                 .:smNNNNNNNNs
         `sNNNs:`smNNmdys+`       `+sydmNNNNNNNNNNs`
          `omNNmo.`hmNNNm-         -NNNNNNNNNNNNmo`
            -hNNNs`:-+-:           mNNNNNNNNNNh-
              :hNNmyo+!++           dNNNNNNNNh:
                .odNNNNNm           dNNNNNdo.
                   .--nEu |  .   |  RaI--.
    """
    len_right = 6 - len(user_art[0])
    len_left = 6 - len(user_art[1])
    len_nose = 6 - len(user_art[2])
    len_mouth = 6 - len(user_art[3])

    if counter == 0:
        octocat_image = octocat_image.replace("N","~")
    if counter == 1:
        octocat_image = octocat_image.replace("N","=")
    if counter == 2:
        octocat_image = octocat_image.replace("N","#")
    if counter == 3:
        octocat_image = octocat_image.replace("N","%")

    octocat_image = octocat_image.format(user_art[0], user_art[1], user_art[2], user_art[3])
    octocat_image = octocat_image.replace("1","{}")
    octocat_image = octocat_image.format(" "*len_right, " "*len_left, " "*len_nose, " "*len_mouth)
    print octocat_image

def octocat_game():
    octocat_image =    """
                     `:+syhdmNNNmdhys+:`
                 `:sdNNNNNNNNNNNNNNNNNNNds:`
               -smNNNNNNNNNNNNNNNNNNNNNNNNNms-
             :hNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNh:
           .sNNNNNy+oydmNN-Octocat-NNmdyo+yNNNNNy.
          -dNNNNNN.   `-++/::---::/++-`   .NNNNNNd-
         -mNNNNNNN.                       .NNNNNNNm-
        `dNNNNNNNd.                       .dNNNNNNNd`
        +NNNNNNNh`                         `hNNNNNNN+
        hNNNNNNNx                           :NNNNNNNh
        nNNNNNNN.                           .NNNNNNNN
        mNNNNNNNk                           /NNNNNNNm
        yNNNNNNNh`                         `hNNNNNNNy
        :NNNNNNNNh-                       -hNNNNNNNN:
         sNNNNmmNNms:.                 .:smNNNNNNNNs
         `sNNNs:`smNNmdys+`       `+sydmNNNNNNNNNNs`
          `omNNmo.`hmNNNm-         -NNNNNNNNNNNNmo`
            -hNNNs`:-+-:           mNNNNNNNNNNh-
              :hNNmyo+/++           dNNNNNNNNh:
                .odNNNNNm           dNNNNNdo.
                   ./NEmU |  .   |  RmAI/.
    """
    
    octocat_image = octocat_image.replace("N","-")
    counter = 0
    print octocat_image
    counter = -1
    Instructions_draw = ["e.g = (<0>) \nPlease... Draw Octocat an eye :",
                            "e.g = (<x>) \n       Nice! draw another one :",
                                "e.g = ^-^ \n              Epic nose job!! :",
                                    "e.g = >{W}< \n                Nom nom nom!! :"]
    for user_drawing in user_art:
        counter += 1
        User_in = raw_input(Instructions_draw[counter])
        while len(User_in) > 6:
            print "Sorry, can only take up to 6 characters."
            User_in = raw_input("              Please try again:")
        user_art[counter] = User_in
        user_art[counter] = user_art[counter].replace("1","|")
        user_art[counter] = user_art[counter].replace("{","[")  #1 and {} are used for creating new format
        user_art[counter] = user_art[counter].replace("}","]")
        printer(counter)
    print "Nice Octocat! Another one?"

octocat_game()
