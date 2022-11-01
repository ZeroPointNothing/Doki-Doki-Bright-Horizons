label mod_script:
    scene bg black_bg
    stop music
    "Note: This mod was a mere test of skills. Do not expect it to be super complicated or amazing."
    "This was just for fun, and I hope you can enjoy this as much as I did making it."
    "Have fun, [player]!"
    pause 1

    scene bg bedroom with dissolve_scene_full
    play music t2
    mc "Ughh..."
    "I reluctantly rise out of bed, my body still begging me to close my eyes."
    mc "What time is it..."
    "I check the clock to see that it is 9:32. I would then begin to panic, only to quickly see the word \"Sunday\"."
    "I then see my phone screen light up and several notifications."
    "A few of them from my friend Sayori."
    mc "I should probably check those before she breaks down my door..."
    "I roll over on my bed to reach my phone. Grabbing it, I turned the screen on and unlocked it."
    $ s_name = "Sayori"
    s "{i}[player]!!! Helloooooooo?!!!{/i}"
    "All 13 messages except for the first one were very similar to these. It was clear she wanted my attention."
    mc "{i}Sayori, you don't have to message me 13 times.{/i}"
    "After a few seconds, she responded." 
    s "{i}{b}There{/b} you are! I've been waiting all morning!{/i}"
    mc "{i}Wait, you didn't sleep in today?{/i}"
    s "{i}Umm... Of course not! Today is too important to sleep in!{/i}"
    mc "{i}What's today?{/i}"
    s "{i}...{/i}{w=1}{nw}"
    s "{i}Did you really forget?{/i}"
    mc "{i}Uhhhhhhhhhh. No.{/i}"
    "I lied."
    s "{i}You promised me you'd remember!!{/i}"
    mc "{i}I was busy, okay?!{/i}"
    s "{i}Busy watching anime...{/i}"
    "I could practically see Sayori's pouting face from where I lie."
    
    
    call not_fns
    
    
    
    
    
    
    
    
    
label not_fns:
    scene bg black_bg
    stop music
    "Unfortunately, you have reached the current end of the script."
    "I am actively working on this, however, so feel free to check the GitHub and update this occasionally!"
    
    $ renpy.quit()