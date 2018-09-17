.class public Lcom/aces/tv/XBMCInputDeviceListener;
.super Ljava/lang/Object;
.source "XBMCInputDeviceListener.java"

# interfaces
.implements Landroid/hardware/input/InputManager$InputDeviceListener;


# direct methods
.method public constructor <init>()V
    .locals 0

    .prologue
    .line 6
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method native _onInputDeviceAdded(I)V
.end method

.method native _onInputDeviceChanged(I)V
.end method

.method native _onInputDeviceRemoved(I)V
.end method

.method public onInputDeviceAdded(I)V
    .locals 0

    .prologue
    .line 15
    invoke-virtual {p0, p1}, Lcom/aces/tv/XBMCInputDeviceListener;->_onInputDeviceAdded(I)V

    .line 16
    return-void
.end method

.method public onInputDeviceChanged(I)V
    .locals 0

    .prologue
    .line 21
    invoke-virtual {p0, p1}, Lcom/aces/tv/XBMCInputDeviceListener;->_onInputDeviceChanged(I)V

    .line 22
    return-void
.end method

.method public onInputDeviceRemoved(I)V
    .locals 0

    .prologue
    .line 27
    invoke-virtual {p0, p1}, Lcom/aces/tv/XBMCInputDeviceListener;->_onInputDeviceRemoved(I)V

    .line 28
    return-void
.end method
