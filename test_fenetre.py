from raylib.static import *

InitWindow(800, 450, b"Hello Raylib")
SetTargetFPS(60)

camera = ffi.new("struct Camera3D *", [[18.0, 16.0, 18.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0])
SetCameraMode(camera[0], CAMERA_ORBITAL)

while not WindowShouldClose():
    UpdateCamera(camera)
    BeginDrawing()
    ClearBackground(RAYWHITE)
    BeginMode3D(camera[0])
    DrawGrid(20, 1.0)
    EndMode3D()
    DrawText(b"Hellow World", 190, 200, 20, VIOLET)
    EndDrawing()
CloseWindow()