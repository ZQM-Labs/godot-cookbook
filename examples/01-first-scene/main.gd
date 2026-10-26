extends Control

var activations: int = 0
var counter_label: Label
var status_label: Label

func _ready() -> void:
	_build_ui()

func _build_ui() -> void:
	var margin := MarginContainer.new()
	margin.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	margin.add_theme_constant_override("margin_left", 32)
	margin.add_theme_constant_override("margin_top", 24)
	margin.add_theme_constant_override("margin_right", 32)
	margin.add_theme_constant_override("margin_bottom", 24)
	add_child(margin)

	var center := CenterContainer.new()
	center.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	center.size_flags_vertical = Control.SIZE_EXPAND_FILL
	margin.add_child(center)

	var stack := VBoxContainer.new()
	stack.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	stack.add_theme_constant_override("separation", 18)
	center.add_child(stack)

	var title := Label.new()
	title.text = "First playable scene"
	title.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	title.add_theme_font_size_override("font_size", 30)
	stack.add_child(title)

	var instructions := Label.new()
	instructions.text = "Activate the button with a click, tap, or keyboard to advance the counter."
	instructions.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	instructions.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	stack.add_child(instructions)

	var button := Button.new()
	button.text = "Activate"
	button.custom_minimum_size = Vector2(0, 56)
	button.focus_mode = Control.FOCUS_ALL
	button.pressed.connect(_on_activate)
	stack.add_child(button)

	counter_label = Label.new()
	counter_label.text = "Activations: 0"
	counter_label.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	counter_label.add_theme_font_size_override("font_size", 24)
	stack.add_child(counter_label)

	status_label = Label.new()
	status_label.text = "Ready. Activations: 0."
	status_label.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	status_label.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	stack.add_child(status_label)

	button.grab_focus()

func _on_activate() -> void:
	activations += 1
	counter_label.text = "Activations: %d" % activations
	status_label.text = "Ready. Activations: %d." % activations
