import pygame.midi

pygame.init()
X = 400
Y = 400
window = pygame.display.set_mode(size=(X, Y))
pygame.display.set_caption('MIDI Keyboard')
pygame.midi.init()
midiOutput = pygame.midi.Output(pygame.midi.get_default_output_id())
instrument = 0
midiOutput.set_instrument(instrument)
octave = 0
volume = 127

white = (255, 255, 255)
black = (0, 0, 0)
print(pygame.font.get_fonts())
font = pygame.font.SysFont('arial', 20)
text = font.render('Q and W to change instrument: ' + str(instrument) + '', True, black, white)
text1 = font.render('Z and X to change octave', True, black, white)
text2 = font.render('C and V to alter the volume: ' + str(volume * 100 / 127) + '', True, black, white)
textRect = text.get_rect()
textRect1 = text1.get_rect()
textRect2 = text2.get_rect()
textRect.center = (X // 2, Y // 4)
textRect1.center = (X // 2, Y * 2 // 4)
textRect2.center = (X // 2, Y * 3 // 4)


def setting(event):
    global volume
    global octave
    global instrument
    global midiOutput

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_z and octave < 7:
            octave += 1
            midiOutput.close()
            midiOutput = pygame.midi.Output(pygame.midi.get_default_output_id())
            midiOutput.set_instrument(instrument)
        if event.key == pygame.K_x and octave > -7:
            octave -= 1
            midiOutput.close()
            midiOutput = pygame.midi.Output(pygame.midi.get_default_output_id())
            midiOutput.set_instrument(instrument)
        if event.key == pygame.K_v and volume < 127:
            volume += 10
        if event.key == pygame.K_c and volume > 0:
            volume -= 10
        if event.key == pygame.K_q and instrument > 0:
            instrument -= 1
            midiOutput.close()
            midiOutput = pygame.midi.Output(0)
            midiOutput.set_instrument(instrument)
        if event.key == pygame.K_w and instrument < 127:
            instrument += 1
            midiOutput.close()
            midiOutput = pygame.midi.Output(pygame.midi.get_default_output_id())
            midiOutput.set_instrument(instrument)

    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
        midiOutput.close()
        pygame.midi.quit()
        pygame.quit()
        quit()

    return


def playSound(event):
    global volume
    global place

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            midiOutput.note_on(place - 8, volume)
        if event.key == pygame.K_s:
            midiOutput.note_on(place - 7, volume)
        if event.key == pygame.K_e:
            midiOutput.note_on(place - 6, volume)
        if event.key == pygame.K_d:
            midiOutput.note_on(place - 5, volume)
        if event.key == pygame.K_r:
            midiOutput.note_on(place - 4, volume)
        if event.key == pygame.K_f:
            midiOutput.note_on(place - 3, volume)
        if event.key == pygame.K_t:
            midiOutput.note_on(place - 2, volume)
        if event.key == pygame.K_g:
            midiOutput.note_on(place - 1, volume)
        if event.key == pygame.K_h:
            midiOutput.note_on(place, volume)
        if event.key == pygame.K_u:
            midiOutput.note_on(place + 1, volume)
        if event.key == pygame.K_j:
            midiOutput.note_on(place + 2, volume)
        if event.key == pygame.K_i:
            midiOutput.note_on(place + 3, volume)
        if event.key == pygame.K_k:
            midiOutput.note_on(place + 4, volume)
        if event.key == pygame.K_l:
            midiOutput.note_on(place + 5, volume)
        if event.key == pygame.K_p:
            midiOutput.note_on(place + 6, volume)
        if event.key == pygame.K_n:
            midiOutput.note_on(place + 7, volume)
        if event.key == pygame.K_m:
            midiOutput.note_on(place + 8, volume)

    if event.type == pygame.KEYUP:

        if event.key == pygame.K_a:
            midiOutput.note_off(place - 8, volume)
        if event.key == pygame.K_s:
            midiOutput.note_off(place - 7, volume)
        if event.key == pygame.K_e:
            midiOutput.note_off(place - 6, volume)
        if event.key == pygame.K_d:
            midiOutput.note_off(place - 5, volume)
        if event.key == pygame.K_r:
            midiOutput.note_off(place - 4, volume)
        if event.key == pygame.K_f:
            midiOutput.note_off(place - 3, volume)
        if event.key == pygame.K_t:
            midiOutput.note_off(place - 2, volume)
        if event.key == pygame.K_g:
            midiOutput.note_off(place - 1, volume)
        if event.key == pygame.K_h:
            midiOutput.note_off(place, volume)
        if event.key == pygame.K_u:
            midiOutput.note_off(place + 1, volume)
        if event.key == pygame.K_j:
            midiOutput.note_off(place + 2, volume)
        if event.key == pygame.K_i:
            midiOutput.note_off(place + 3, volume)
        if event.key == pygame.K_k:
            midiOutput.note_off(place + 4, volume)
        if event.key == pygame.K_l:
            midiOutput.note_off(place + 5, volume)
        if event.key == pygame.K_p:
            midiOutput.note_off(place + 6, volume)
        if event.key == pygame.K_n:
            midiOutput.note_off(place + 7, volume)
        if event.key == pygame.K_m:
            midiOutput.note_off(place + 8, volume)

        return


while True:
    place = 68 - octave * 8
    text = font.render('Q and W to change instrument: ' + str(instrument) + '', True, black, white)
    text1 = font.render('Z and X to change octave: ' + str(octave) + '', True, black, white)
    text2 = font.render('C and V to alter the volume: ' + str(volume * 100 // 127) + '', True, black, white)
    window.fill(white)
    window.blit(text, textRect)
    window.blit(text1, textRect1)
    window.blit(text2, textRect2)
    pygame.display.update()
    pygame.time.wait(16)
    for event in pygame.event.get():
        setting(event)
        playSound(event)
