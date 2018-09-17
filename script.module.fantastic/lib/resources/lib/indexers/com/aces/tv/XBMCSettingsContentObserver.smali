.class public Lcom/aces/tv/XBMCSettingsContentObserver;
.super Landroid/database/ContentObserver;
.source "XBMCSettingsContentObserver.java"


# static fields
.field private static final TAG:Ljava/lang/String; = "kodi"


# instance fields
.field context:Landroid/content/Context;

.field previousVolume:I


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/os/Handler;)V
    .locals 2

    .prologue
    .line 21
    invoke-direct {p0, p2}, Landroid/database/ContentObserver;-><init>(Landroid/os/Handler;)V

    .line 22
    iput-object p1, p0, Lcom/aces/tv/XBMCSettingsContentObserver;->context:Landroid/content/Context;

    .line 24
    iget-object v0, p0, Lcom/aces/tv/XBMCSettingsContentObserver;->context:Landroid/content/Context;

    const-string v1, "audio"

    invoke-virtual {v0, v1}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/media/AudioManager;

    .line 25
    const/4 v1, 0x3

    invoke-virtual {v0, v1}, Landroid/media/AudioManager;->getStreamVolume(I)I

    move-result v0

    iput v0, p0, Lcom/aces/tv/XBMCSettingsContentObserver;->previousVolume:I

    .line 26
    return-void
.end method


# virtual methods
.method native _onVolumeChanged(I)V
.end method

.method public onChange(Z)V
    .locals 1

    .prologue
    .line 34
    const/4 v0, 0x0

    invoke-virtual {p0, p1, v0}, Lcom/aces/tv/XBMCSettingsContentObserver;->onChange(ZLandroid/net/Uri;)V

    .line 35
    return-void
.end method

.method public onChange(ZLandroid/net/Uri;)V
    .locals 3

    .prologue
    .line 40
    invoke-super {p0, p1}, Landroid/database/ContentObserver;->onChange(Z)V

    .line 42
    const-string v0, "kodi"

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "Setting changed: "

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {p2}, Landroid/net/Uri;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 44
    const-string v0, "content://settings/system/volume_music_speaker"

    invoke-static {v0}, Landroid/net/Uri;->parse(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v0

    invoke-virtual {p2, v0}, Landroid/net/Uri;->compareTo(Landroid/net/Uri;)I

    move-result v0

    if-eqz v0, :cond_0

    const-string v0, "content://settings/system/volume_music_hdmi"

    invoke-static {v0}, Landroid/net/Uri;->parse(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v0

    invoke-virtual {p2, v0}, Landroid/net/Uri;->compareTo(Landroid/net/Uri;)I

    move-result v0

    if-nez v0, :cond_1

    .line 49
    :cond_0
    iget-object v0, p0, Lcom/aces/tv/XBMCSettingsContentObserver;->context:Landroid/content/Context;

    const-string v1, "audio"

    invoke-virtual {v0, v1}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/media/AudioManager;

    .line 51
    const/4 v1, 0x3

    invoke-virtual {v0, v1}, Landroid/media/AudioManager;->getStreamVolume(I)I

    move-result v0

    .line 53
    iget v1, p0, Lcom/aces/tv/XBMCSettingsContentObserver;->previousVolume:I

    if-eq v0, v1, :cond_1

    .line 57
    :try_start_0
    invoke-virtual {p0, v0}, Lcom/aces/tv/XBMCSettingsContentObserver;->_onVolumeChanged(I)V

    .line 58
    iput v0, p0, Lcom/aces/tv/XBMCSettingsContentObserver;->previousVolume:I
    :try_end_0
    .catch Ljava/lang/UnsatisfiedLinkError; {:try_start_0 .. :try_end_0} :catch_0

    .line 66
    :cond_1
    :goto_0
    return-void

    .line 60
    :catch_0
    move-exception v0

    .line 62
    const-string v0, "XBMCSettingsContentObserver"

    const-string v1, "Native not registered"

    invoke-static {v0, v1}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_0
.end method
