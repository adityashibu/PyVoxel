from settings import *
import moderngl as mgl
import pygame as pg
import sys


class VoxelEngine:
    def __init__(self):
        # Initialize the pygame submodule
        pg.init()
        # Set the below OpenGL Attributes
        # 1. Configure the OpenGL version to use
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        # 2. Configure OpenGl to use the latest and best features
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        # 3. Set depth buffer as 24 bits, ie depth in a 3D view
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)

        # Set the window resolution and create the OpenGL context
        pg.display.set_mode(WIN_RES, flags=pg.OPENGL | pg.DOUBLEBUF)
        # Call the create_context() method to get access to create the context
        self.ctx = mgl.create_context()

        # Initialize fragment depth testing
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)
        # Enable automatic garbage collection of unused OpenGL objects
        self.ctx.gc_mode = 'auto'

        # Object to keep track of time
        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.time = 0

        # Flag to check if our application is running
        self.is_running = True
    # Update method to update the state of objects
    def update(self):
        self.delta_time = self.clock.tick()
        self.time = pg.time.get_ticks() * 0.001
        pg.display.set_caption(f'{self.clock.get_fps() :.0f}')
    # Method for rendering the objects
    def render(self):
        self.ctx.clear(color=BG_COLOR)
        pg.display.flip()
    # Method for handling events
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False
    # Method to call the main application loop
    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
        pg.quit()
        sys.exit()

# Create instance of the class and call the run method
if __name__ == '__main__':
    app = VoxelEngine()
    app.run()