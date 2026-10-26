extends SceneTree

func _initialize() -> void:
	call_deferred("_run_smoke_test")


func _run_smoke_test() -> void:
	var packed_scene := load("res://main.tscn") as PackedScene
	if packed_scene == null:
		_fail("Could not load res://main.tscn.")
		return

	var scene := packed_scene.instantiate()
	root.add_child(scene)
	await process_frame

	var buttons := scene.find_children("*", "Button", true, false)
	if buttons.size() != 1:
		_fail("Expected exactly one runtime Button; found %d." % buttons.size())
		return

	var activate_button := buttons[0] as Button
	if activate_button.text != "Activate":
		_fail("Unexpected button text: %s." % activate_button.text)
		return

	var counter_label: Label
	var status_label: Label
	for node in scene.find_children("*", "Label", true, false):
		var label := node as Label
		if label.text == "Activations: 0":
			counter_label = label
		elif label.text == "Ready. Activations: 0.":
			status_label = label

	if counter_label == null or status_label == null:
		_fail("Initial counter and status labels were not created.")
		return

	activate_button.emit_signal("pressed")
	await process_frame

	if counter_label.text != "Activations: 1":
		_fail("Counter did not update after activation: %s." % counter_label.text)
		return
	if status_label.text != "Ready. Activations: 1.":
		_fail("Status did not update after activation: %s." % status_label.text)
		return

	print("Godot runtime smoke test passed: scene loads and activation updates visible state.")
	quit(0)


func _fail(message: String) -> void:
	push_error(message)
	quit(1)
